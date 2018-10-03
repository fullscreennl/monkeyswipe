//
//  OOOGameView.m
//  oneonone
//
//  Created by Johan ten Broeke on 2/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

// enums that will be used as tags

#import "OOOGameView.h"
#import "OOONotificationNames.h"
#import "OOOGameSprite.h"
#import "OOOBackgroundLayer.h"
#import "OOOLevelManager.h"
#import "OOODebugDrawLayer.h"
#import "SimpleAudioEngine.h"
#import "OOOJointLayer.h"
#import "OOOQuitLevelLayer.h"
#import "OOOGameSettingsManager.h"
#import "OOOTextureCacheManager.h"

@implementation OOOGameView

+(id) sceneWithLevelId:(NSString *)level_id
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	OOOGameView *layer = [OOOGameView node];
	[layer buildLevel:level_id];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

+(id) sceneWithDictionary:(NSDictionary *)dict
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	OOOGameView *layer = [OOOGameView node];
	[layer buildLevelWithDictionary:dict];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		gameModel = [[OOOGameModel alloc] init];
		// enable touches
		self.isTouchEnabled = YES;
		
		// enable accelerometer
		self.isAccelerometerEnabled = YES;
		
		CGSize screenSize = [CCDirector sharedDirector].winSize;
		CCLOG(@"Screen width %0.2f screen height %0.2f",screenSize.width,screenSize.height);
		
		bgLayer = [OOOBackgroundLayer layer];
		[self addChild: bgLayer z:0 tag:666];

	}	
	return self;
}

-(void)buildLevelWithDictionary:(NSDictionary *)dict{
	level_data_loader = [[OOOLevelData alloc] initWithDict:dict];
	[self drawLevel];	
}

-(void)buildLevel:(NSString *)level_id{
	[level_data_loader release];
	//NSLog(@"level id:%@",level_id);
	level_data_loader = [[OOOLevelData alloc] initWithLevel:level_id];
	[self drawLevel];
}

-(void) drawLevel{
	level_data = [level_data_loader getdata];
	//NSLog(@"leveldata %@ : ",level_data);
	if (level_data) {
		[self drawBackground];
		[self drawJointLayer];
		[self buildSpriteSheets];
		[self enhanceBackground];
		[self drawCompounds];
		[self buildJoints];
		//[self createDebugDraw];
		[self registerContacts];
		[self drawQuitButton];
		[self schedule: @selector(tick:)];	
	}

}

-(void)drawQuitButton{
	OOOQuitLevelLayer *quitLayer = [OOOQuitLevelLayer layer];
	[self addChild: quitLayer z:0 tag:121];
}

-(void)drawJointLayer{
	jointLayer = [OOOJointLayer layer];
	[jointLayer setWorld:(b2World *)[gameModel getWorld]];
	[self addChild: jointLayer z:0 tag:121];
}

-(void)createDebugDraw{
	dbDrawLayer = [OOODebugDrawLayer layer];
	[dbDrawLayer setWorld:(b2World *)[gameModel getWorld]];
	[self addChild: dbDrawLayer z:0 tag:121];
}

- (void) onEnterTransitionDidFinish{
	//NSLog(@">> onEnterTransitionDidFinish %@",self);
	
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"levelLoaded" 
					   object:nil 
					   userInfo:nil]];
	
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onEnemyHit:) 
												 name:@"onEnemyHit" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onHeroHit:) 
												 name:@"onHeroHit" 
											   object:nil];
	
	[gameModel onEnterTransitionDidFinish];
	
	
}

-(void) onHeroHit:(NSNotification *) note{
	if (CCRANDOM_0_1() > .5 ? 0:1){
		[[SimpleAudioEngine sharedEngine] playEffect:@"monkey_hi.wav"];
	}else{	
		[[SimpleAudioEngine sharedEngine] playEffect:@"monkey_ha.wav"];
	}
}

-(void) onEnemyHit:(NSNotification *) note{
	if (CCRANDOM_0_1() > .5 ? 0:1){
		[[SimpleAudioEngine sharedEngine] playEffect:@"sfx_enemy_bounce_a.wav"];
	}else{	
		[[SimpleAudioEngine sharedEngine] playEffect:@"sfx_enemy_bounce_b.wav"];
	}
}


-(void)registerContacts{
	NSArray *contacts = [[level_data objectForKey:@"level"] objectForKey:@"contacts"];
	[gameModel registerContacts:contacts];
}

-(void)buildJoints{
	NSArray *joints = [[level_data objectForKey:@"level"] objectForKey:@"joints"];
	int arrayCount = [joints count];
	for (int i = 0; i < arrayCount; i++) {
		if ([[[joints objectAtIndex:i] objectForKey:@"type"]isEqualToString:@"revolute"]){
			[gameModel createRevJoint:[joints objectAtIndex:i]];
		}else if ([[[joints objectAtIndex:i] objectForKey:@"type"]isEqualToString:@"distance"]) {
			[gameModel createDistJoint:[joints objectAtIndex:i]];
		}else if ([[[joints objectAtIndex:i] objectForKey:@"type"]isEqualToString:@"prismatic"]) {
			[gameModel createPrismJoint:[joints objectAtIndex:i]];
		}
	}
}

-(void)drawBackground{
	NSString *bg = nil;
	BOOL isTut = [[OOOLevelManager sharedLevelManager] isTutorial];
	if([[[[OOOGameSettingsManager sharedManager] getSettings] objectForKey:@"doodleStyle"] boolValue]==NO or isTut){
		bg = [[level_data objectForKey:@"level"] objectForKey:@"background"];
	}else{
		bg = @"doodle_bg.png";
	}
	CCSprite *sprite = [CCSprite spriteWithFile:bg];
	[bgLayer addChild:sprite z:0 tag:1];
	sprite.position = ccp(240, 160);
}

-(void)enhanceBackground{
	if ([[[level_data objectForKey:@"level"] objectForKey:@"decals"] isEqualToString:@"dragAndRelease"]) {
		CCSpriteSheet *actor_sheet = (CCSpriteSheet*) [self getChildByTag:6];
		//[actor_sheet addChild:[actor_sheet getChildByTag:<#(int)tag#>
		//CCSpriteFrame *vingerSprite = [[CCSpriteFrameCache sharedSpriteFrameCache] spriteFrameByName:@"vinger_track.png"];
		CCSprite *fingerTrack = [[[CCSprite alloc ]initWithSpriteFrameName: @"vinger_track.png"] autorelease];
		CCSprite *handDown = [[[CCSprite alloc ]initWithSpriteFrameName: @"hand_down.png"] autorelease];
		CCSprite *handUp = [[[CCSprite alloc ]initWithSpriteFrameName: @"hand_up.png"] autorelease];
		[actor_sheet addChild:fingerTrack];
		[actor_sheet addChild:handDown];
		[actor_sheet addChild:handUp];
		float ycorr = -10;
		float xcorr = 85;
		fingerTrack.position =ccp(240.0f + xcorr,180.0f + ycorr);
		handUp.position =ccp(180.0f + xcorr,225.0f  + ycorr);
		handDown.position =ccp(180.0f+ xcorr,225.0f + ycorr );
		
		//handDown move slow
		id action = [CCMoveBy actionWithDuration:2.0f position:ccp(60.0f, 15.0f)];
		id actionEase = [CCEaseInOut actionWithAction:action rate:2];
		
		//handUp moveback
		id action2 = [CCMoveBy actionWithDuration:1.0f position:ccp(-60.0f, -15.0f)];
		id action2Ease = [CCEaseInOut actionWithAction:action2 rate:2];
		
		
		//id seq = [CCSequence actions:[CCDelayTime actionWithDuration:4.0f],action2Ease,[CCCallFunc  ] ,nil];
		//id seq2 = [CCSequence actions:actionEase,[CCDelayTime actionWithDuration:1.0f],nil];
		
		/*
		 handDown fadeIn quick
		 handUp fadeOut semi- quick
		 handUp moveQuick 60,15
		 handDwon move 60, 15
		 handUp fadeIn quick
		 handDown fadeOut quick
		 handUp moveSlow -60, -15
		 handDown moveQuick -60, 15
		 repeatForever.
		 */
		
		//hand fades
		id handFadeOut = [CCFadeOut actionWithDuration:.5f];
		id handFadeOutEase = [CCEaseOut actionWithAction:handFadeOut  rate:2.0];
		id handFadeIn = [CCFadeIn actionWithDuration:.5f];
		id handFadeInEase = [CCEaseOut actionWithAction:handFadeIn  rate:2.0];
		id handFadeOut2 = [CCFadeOut actionWithDuration:.5f];
		id handFadeOutEase2 = [CCEaseOut actionWithAction:handFadeOut2  rate:2.0];
		id handFadeIn2 = [CCFadeIn actionWithDuration:.5f];
		id handFadeInEase2 = [CCEaseOut actionWithAction:handFadeIn2  rate:2.0];
		//handUp sequence
		id handUpFastMove = [CCMoveBy actionWithDuration:2.0f position:ccp(60.0f, 15.0f)];
		id handUpSeq = [CCSequence actions:handFadeOutEase,handUpFastMove, handFadeInEase,action2Ease, nil];
		
		id handDownFastMove = [CCMoveBy actionWithDuration:1.0f position:ccp(-60.0f, -15.0f)];
		
		id handDownSeq = [CCSequence actions:handFadeInEase2, actionEase, handFadeOutEase2, handDownFastMove, nil]; 
		[handDown runAction:[CCRepeatForever actionWithAction:handDownSeq]];
		[handUp runAction:[CCRepeatForever actionWithAction:handUpSeq]];
	}
}



-(void) buildSpriteSheets{
	NSArray *sheets = [[level_data objectForKey:@"level"] objectForKey:@"sheets"];
	int arrayCount = [sheets count];
	for (int i = 0; i < arrayCount; i++) {
		NSString *sheetname = nil;
		if([[[[OOOGameSettingsManager sharedManager] getSettings] objectForKey:@"doodleStyle"] boolValue]==NO){
			sheetname = [[sheets objectAtIndex:i] objectForKey:@"atlas"];
		}else{
			sheetname = [[sheets objectAtIndex:i] objectForKey:@"atlas2"];
		}
		
		NSString *img = [sheetname stringByAppendingString:@".png"];
		NSString *atlas = [sheetname stringByAppendingString:@".plist"];
		NSNumber *_id = [[sheets objectAtIndex:i] objectForKey:@"id"];
		CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:img capacity:150];
		
		[[OOOTextureCacheManager sharedTextureCacheManager]addAtlas:atlas];
		//[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:atlas];

		[self addChild:sheet z:0 tag:[_id intValue]];
	}
}

-(void) drawCompounds{
	NSArray *comps = [[level_data objectForKey:@"level"] objectForKey:@"compounds"];
	int arrayCount = [comps count];
	for (int i = 0; i < arrayCount; i++) {
		[self drawCompoundWithDict:[comps objectAtIndex:i]];
	}
}

-(void)drawCompoundWithDict: (NSDictionary *)dict{
	// get data
	float w = [[[dict objectForKey:@"body"] objectForKey:@"width"]floatValue];
	float h = [[[dict objectForKey:@"body"] objectForKey:@"height"]floatValue];
	float x = [[[dict objectForKey:@"body"] objectForKey:@"x"]floatValue];
	float y = [[[dict objectForKey:@"body"] objectForKey:@"y"]floatValue];
	
	NSString *firstFrame = [[dict objectForKey:@"body"] objectForKey:@"firstFrame"];
	NSNumber *sheet_id = [[dict objectForKey:@"body"] objectForKey:@"sheet_id"];
	NSNumber *spr_id = [[dict objectForKey:@"body"] objectForKey:@"id"];
	NSString *name = [[dict objectForKey:@"body"] objectForKey:@"name"];
	
	NSString *classname = [[dict objectForKey:@"body"] objectForKey:@"classname"];
	
	if ([classname isEqualToString:@""]) {
		classname = nil;
	}

	// get sprite sheet
	CCSpriteSheet *actor_sheet = (CCSpriteSheet*) [self getChildByTag:[sheet_id intValue]];
	
	// create sprite
	OOOGameSprite *sprite;
	
	if (classname) {
		//NSLog(@"instance name %@",name);
		//NSLog(@"class name %@",classname);
		sprite = [[NSClassFromString(classname) alloc] initWithSheet:actor_sheet andName:name andKeyFrame:firstFrame];
		[sprite setClassName:classname];
	}else{
		sprite = [[OOOGameSprite alloc] initWithSheet:actor_sheet andName:name andKeyFrame:firstFrame]; 
		[sprite setClassName:@"BaseClass"];
	}
	[sprite setHeight: h];
	[sprite setWidth: w];
	sprite.position = CGPointMake(x, y);
	[actor_sheet addChild:sprite z:0 tag:[spr_id intValue]];

	if([dict objectForKey:@"shapes"]){
		b2Body *body = [gameModel createCompoundPhysicsWithSpriteAttached:sprite andDict:dict];
		[sprite setB2Body:body];
	}
	[sprite release];
}

- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{

	for( UITouch *touch in touches ) {
		if (touch == currentTouch){
			CGPoint location = [touch locationInView: [touch view]];
			
			location = [[CCDirector sharedDirector] convertToGL: location];
			
			float _dx = currentLocation.x - location.x;
			float _dy = currentLocation.y - location.y;								

			[[OOOLevelManager sharedLevelManager] addSwipe];
			
			NSDictionary *userinfo = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithFloat:_dx], @"dx", [NSNumber numberWithFloat:_dy], @"dy",nil];
			[userinfo retain];
			
			[[NSNotificationCenter defaultCenter] 
			 postNotification:[NSNotification 
							   notificationWithName:@"onSwipe" 
							   object:nil 
							   userInfo:userinfo]];
			
			[userinfo release];
			/*
			*/
		}
	}
}


- (void)ccTouchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
	//Add a new body/atlas sprite at the touched location
	for( UITouch *touch in touches ) {
		currentTouch = touch;
		CGPoint location = [touch locationInView: [touch view]];
		
		location = [[CCDirector sharedDirector] convertToGL: location];
		currentLocation = location;
		//NSLog(@"began swipe :x %f  y %f\n\n",location.x,location.y);
	}
}

- (void)accelerometer:(UIAccelerometer*)accelerometer didAccelerate:(UIAcceleration*)acceleration
{	
	//static float prevX=0, prevY=0;
	
	//#define kFilterFactor 0.05f
#define kFilterFactor 1.0f	// don't use filter. the code is here just as an example
	
	float accelX = (float) acceleration.x * 500;
	float accelY = (float) acceleration.y * 500;
	
	//NSLog(@"accel x : %f",accelX);
	//NSLog(@"accel y : %f",accelY);
	
	NSDictionary *userinfo = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithFloat:accelX], @"dx", [NSNumber numberWithFloat:accelY], @"dy",nil];
	[userinfo retain];
	
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onAccel" 
					   object:nil 
					   userInfo:userinfo]];
	
	[userinfo release];
	
}



-(void) tick: (ccTime) dt
{
	[gameModel onGameLoop];
}

-(void)dealloc{
	[[NSNotificationCenter defaultCenter] removeObserver:self]; 
	[level_data_loader release];
	//[level_data release];
	[gameModel release];
	[super dealloc];
}

@end
