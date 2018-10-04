//
//  MainSplash.mm
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 fullscreen. All rights reserved.
//



#import "Settings.h"
//#import "button.h"
#import "MainMenu.h"
#import "SimpleAudioEngine.h"
#import "OOOGameSettingsManager.h"


@implementation Settings

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	Settings *layer = [Settings node];
	
	//BackgroundLayer *bgLayer = [BackgroundLayer layer];
	[scene addChild: layer];
	// return the scene
	return scene;
}


- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	UITouch *touch = [touches anyObject];
	CGPoint location = [touch locationInView: [touch view]];
	//NSLog(@"touches pos: %3f",location.x);
	if (location.y>130.0f and location.y<200.0f) {
		[self toggleSound];
	}else if(location.y>200 ) {
		[self toggleDoodle];
	}
	
}

-(void)toggleSound
{
	if(soundFXMuted == NO){
		[[SimpleAudioEngine sharedEngine] playEffect:@"switch.wav"];
		soundFXMuted = YES;
		[SimpleAudioEngine sharedEngine].muted = YES;
	}else{
		soundFXMuted = NO;
		[SimpleAudioEngine sharedEngine].muted = NO;
		[[SimpleAudioEngine sharedEngine] playEffect:@"switch.wav"];
	}
	
	[self setSwirlPos:soundFXMuted];
}


-(void)toggleDoodle
{
	if(doodleStyle == NO){
		doodleStyle = YES;
	}else{
		doodleStyle = NO;
	}
	
	[self setSwirlPos:soundFXMuted];
}


-(void)setSwirlPos:(BOOL)_soundState
{
	if(_soundState == YES){
		//off
		
		//swirlSprite.position = ccp(314.0f, 83.0f);
		swirlSprite.position = ccp(398, 160);
	}else{
		//on
		friendSilentSpr.opacity = 0;
		friendloudSpr.opacity = 255;
		//swirlSprite.position = ccp( 220.0f , 83.0f);
		swirlSprite.position = ccp(314, 160);
	}
	
	if(doodleStyle == NO){
		swirlSprite2.position = ccp(398, 60);
		if(_soundState==YES){
			friendSilentSpr.opacity = 255;
			friendloudSpr.opacity = 0;
			friendDoodleloudSpr.opacity = 0;
			friendDoodleSilentSpr.opacity = 0;
		}else{
			friendSilentSpr.opacity = 0;
			friendloudSpr.opacity = 255;
			friendDoodleloudSpr.opacity = 0;
			friendDoodleSilentSpr.opacity = 0;
		}
	}else{
		swirlSprite2.position = ccp(314, 60);
		if(_soundState==YES){
			friendSilentSpr.opacity = 0;
			friendloudSpr.opacity = 0;
			friendDoodleloudSpr.opacity = 0;
			friendDoodleSilentSpr.opacity = 255;
		}else{
			friendSilentSpr.opacity = 0;
			friendloudSpr.opacity = 0;
			friendDoodleloudSpr.opacity = 255;
			friendDoodleSilentSpr.opacity = 0;
		}
	}
	/*writing to local settings.plist*/
	
	
	NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
	NSString *documentsDirectory = [paths objectAtIndex:0];
	NSString *appSettingsPath = [documentsDirectory stringByAppendingPathComponent:@"settings.plist"];
	[settings setObject:[NSNumber numberWithBool:soundFXMuted] forKey:@"soundFXMuted"];
	[settings setObject:[NSNumber numberWithBool:doodleStyle] forKey:@"doodleStyle"];
	[settings writeToFile:appSettingsPath atomically:YES];
	[[OOOGameSettingsManager sharedManager] setSettings:settings];
	
}

-(id) init
{
	if( (self=[super init])) {
		self.isTouchEnabled = YES;
		
		NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
		NSString *documentsDirectory = [paths objectAtIndex:0];
		NSString *file = [documentsDirectory stringByAppendingPathComponent:@"settings.plist"];
		
		settings = [[NSMutableDictionary dictionaryWithContentsOfFile:file] retain];
		//NSLog(@"settings: %@",settings);
		if(settings == nil){
			NSString *file = [[NSBundle mainBundle] pathForResource:@"settings" ofType:@"plist"];
			settings = [[NSMutableDictionary dictionaryWithContentsOfFile:file] retain];
		}
		soundFXMuted = [[settings objectForKey:@"soundFXMuted"] boolValue];
		doodleStyle =[[settings objectForKey:@"doodleStyle"] boolValue];
		CGSize screenSize = [CCDirector sharedDirector].winSize;
		
		
		CCSprite *sprite = [CCSprite spriteWithFile:@"settings_newcolor.png"];
		[self addChild:sprite];
		sprite.position = ccp( screenSize.width/2, screenSize.height/2);
		
		swirlSprite = [CCSprite spriteWithFile:@"selectionswirl.png"];
		[self addChild:swirlSprite];
		swirlSprite2 = [CCSprite spriteWithFile:@"selectionswirl.png"];
		[self addChild:swirlSprite2];

		
		
		CCMenu *menu = [CCMenu menuWithItems:nil];
		//menu.position = ccp(240, 160);
		
		CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
		[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
		[self addChild:sheet z:0 tag:674];
		
		CCSprite *upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn.png"];
		CCSprite *downsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_down.png"];
		CCSprite *disabledsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis.png"];
		//CCSprite *upsprite = [CCSprite spriteWithFile:@"generic_btn.png"];
		CCMenuItem *subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
													  selectedSprite:downsprite 
													  disabledSprite:disabledsprite 
															  target:self 
															selector:@selector(goBack:)];	
		
		NSString *text = @"MENU";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		CCBitmapFontAtlas *textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2)-20 ,round( subItem.contentSize.height / 2) - 8);
		
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
		
		[menu addChild:subItem z:1 tag:1];
		subItem.position = ccp(100, 120);
		CGPoint dstPoint = subItem.position;
		int offset = round(screenSize.width/2) + 150;
		id movebtn = [CCMoveBy actionWithDuration:2 position:ccp(dstPoint.x - offset,0)];
		id actionbtn = [CCEaseElasticOut actionWithAction:movebtn period:0.3f];
		
		subItem.position = ccp( dstPoint.x + offset, dstPoint.y);
		[subItem runAction:actionbtn];
		
		[self addChild:menu];		
		
		///hovering caterpillar
		friendloudSpr = [CCSprite spriteWithFile:@"friend_loud.png"];
		friendSilentSpr = [CCSprite spriteWithFile:@"friend_silent.png"];
		friendDoodleloudSpr = [CCSprite spriteWithFile:@"friend_doodle_loud.png"];
		friendDoodleSilentSpr = [CCSprite spriteWithFile:@"friend_doodle_silent.png"];
		friendloudSpr.scale = .6;
		friendSilentSpr.scale = .6;
		friendSilentSpr.opacity = 0;
		[self addChild:friendloudSpr];
		[self addChild:friendSilentSpr];
		[self addChild:friendDoodleloudSpr];
		[self addChild:friendDoodleSilentSpr];
		
		friendloudSpr.position = ccp(79.0f, 85.0f);
		friendSilentSpr.position = ccp(79.0f, 85.0f);
		friendDoodleSilentSpr.position = ccp(79.0f, 85.0f);
		friendDoodleloudSpr.position = ccp(79.0f, 85.0f);
		/*
		id fadeOut_action = [CCFadeOut actionWithDuration:3 ];
		id ease_alpha_action = [CCEaseInOut actionWithAction:fadeOut_action rate:2];
		id easeBack_alpha_action = [ease_alpha_action reverse];
		id alphaseq = [CCSequence actions:ease_alpha_action, easeBack_alpha_action, nil];
		[dropshadowSpr runAction:[CCRepeatForever actionWithAction:alphaseq]];
		*/
		
		id move_action = [CCMoveBy actionWithDuration:2 position:ccp(0.0f,10.0f)];
		id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
		id easeBack_action = [ease_action reverse];
		id seq = [CCSequence actions:ease_action, easeBack_action, nil];
		[friendloudSpr runAction:[CCRepeatForever actionWithAction:seq]];
		id move_action2 = [CCMoveBy actionWithDuration:2 position:ccp(0.0f,10.0f)];
		id ease_action2 = [CCEaseInOut actionWithAction:move_action2 rate:2];
		id easeBack_action2 = [ease_action2 reverse];
		id seq2 = [CCSequence actions:ease_action2, easeBack_action2, nil];
		[friendSilentSpr runAction:[CCRepeatForever actionWithAction:seq2]];
		id move_action3 = [CCMoveBy actionWithDuration:2 position:ccp(0.0f,10.0f)];
		id ease_action3 = [CCEaseInOut actionWithAction:move_action3 rate:2];
		id easeBack_action3 = [ease_action3 reverse];
		id seq3 = [CCSequence actions:ease_action3, easeBack_action3, nil];
		[friendDoodleloudSpr runAction:[CCRepeatForever actionWithAction:seq3]];
		id move_action4 = [CCMoveBy actionWithDuration:2 position:ccp(0.0f,10.0f)];
		id ease_action4 = [CCEaseInOut actionWithAction:move_action4 rate:2];
		id easeBack_action4 = [ease_action4 reverse];
		id seq4 = [CCSequence actions:ease_action4, easeBack_action4, nil];
		[friendDoodleSilentSpr runAction:[CCRepeatForever actionWithAction:seq4]];
		[self setSwirlPos:soundFXMuted];
	}
	return self;
}	

-(void) goBack: (id)sender
{
	 [[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	 [[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];
}



- (void)dealloc 
{
	[settings release];
	//NSLog(@"deallocing settings");
    [super dealloc];
}


@end
