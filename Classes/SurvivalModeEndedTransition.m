//
//  SurvivalModeEndedTransition.m
//  MonkeySwipe
//
//  Created by Johan ten Broeke on 4/5/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "SurvivalModeEndedTransition.h"
#import "SimpleAudioEngine.h"
#import "OOOLevelManager.h"


@implementation SurvivalModeEndedTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	SurvivalModeEndedTransition *layer = [SurvivalModeEndedTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {	
		bgImage = @"survival_cutscene_bg.png";
		[self drawUI];
		self.isTouchEnabled = YES;
	}
	return self;
}

-(void)drawUI{
	
	CCSprite *bg = [CCSprite spriteWithFile:bgImage];
	bg.position =ccp(240.0f,160.0f);
	[self addChild:bg z:0 tag:2];
	
	NSDictionary *highScores = [[OOOLevelManager sharedLevelManager] getSurvivalScore];
	NSString *levelReached = [[highScores objectForKey:@"level"] stringValue];
	NSString *score = [[highScores objectForKey:@"score"] stringValue];
	NSNumber *swipesUsed = [highScores objectForKey:@"swipes"];
	NSNumber *highScore = [highScores objectForKey:@"highscore"];
	
		
	
	CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
	[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
	[self addChild:sheet z:0 tag:1];
	
	CCSprite *monkeyHand = [CCSprite spriteWithSpriteFrameName:@"monkeyhand.png"];
	monkeyHand.position=ccp(45.0f, 50.0f);
	[self addChild:monkeyHand z:0 tag:3];
	
	id move_action = [CCMoveBy actionWithDuration:1 position:ccp(0.0f,10.0f)];
	id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
	id easeBack_action = [ease_action reverse];
	id seq = [CCSequence actions:ease_action, easeBack_action, nil];
	[monkeyHand runAction:[CCRepeatForever actionWithAction:seq]];
	
	
	//NSLog(@"num stars --> %@",[[OOOLevelManager sharedLevelManager] getNumStarsForPrevLevel]);
	
	CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:score fntFile:@"marker_felt2.fnt"];
	label1.position = ccp( 370, 214);
	//label1.scale = .5;
	[self addChild:label1];
	
	
	if ([highScore intValue]==1 ) {
		CCSprite *highScoreDecal = [CCSprite spriteWithSpriteFrameName:@"highscore_decal2.png"];
		[self addChild:highScoreDecal z:1 tag:1];
		highScoreDecal.position =ccp(377, 222);
	}
	
	//NSNumber *secondsPassed = [[OOOLevelManager sharedLevelManager] getTimeForPrevLevel];
	//NSString *levelReachedLine = [[secondsPassed stringValue] stringByAppendingString:@" s"];
	
	CCLabel *levelReachedLabel = [CCLabel labelWithString:levelReached fontName:@"Marker Felt" fontSize:20.0];
	[levelReachedLabel setColor:ccc3(0,0,0)];
	levelReachedLabel.position =ccp(345.0,158.0);
	[self addChild:levelReachedLabel];
	
	
	
	CCLabel *swipeLabel = [CCLabel labelWithString:[swipesUsed stringValue] fontName:@"Marker Felt" fontSize:20.0];
	[swipeLabel setColor:ccc3(0,0,0)];
	swipeLabel.position =ccp(295.0,180.0);
	[self addChild:swipeLabel];
	
	
	
	
}

- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	UITouch *touch = [touches anyObject];
	CGPoint location = [touch locationInView: [touch view]];
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	//NSLog(@"touches pos: %3f",location.y);
	if(location.y < 100.0f){
		[self goMenu];
	}else{
		[self retry];
	}
}

-(void)retry{
	id functioncall_action = [CCCallFunc actionWithTarget:self selector:@selector(retrySurvival:)];
	id seq2 = [CCSequence actions:[CCDelayTime actionWithDuration: 0.0f],functioncall_action,nil]; 
	[self runAction:seq2];
}

-(void)retrySurvival: (id)sel{
	//NSLog(@"onSurvivalModeEntered");
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onSurvivalModeEntered" 
					   object:nil 
					   userInfo:nil]];
}

-(void)goMenu{
	id functioncall_action = [CCCallFunc actionWithTarget:self selector:@selector(loadMenu:)];
	id seq2 = [CCSequence actions:[CCDelayTime actionWithDuration: 0.0f],functioncall_action,nil]; 
	[self runAction:seq2];
}

-(void)loadMenu: (id)sel{
	//NSLog(@"goMenu");
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onReturnToMainMenu" 
					   object:nil 
					   userInfo:nil]];
}

-(void)dealloc{
	[super dealloc];
}


@end
