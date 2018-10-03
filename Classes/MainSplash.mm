//
//  MainSplash.mm
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "MainSplash.h"
//#import "OpenFeint.h"
//#import "SampleOFDelegate.h"
#import "MainMenu.h"
#import "SimpleAudioEngine.h"
#import <GameKit/GameKit.h>
#import "OOOLevelMap.h"
#import "OOOGameSettingsManager.h"

@implementation MainSplash

+(id) scene
{
	// 'scene' is an autorelease object.
	//CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	//MainSplash *layer = [MainSplash node];
	
	//BackgroundLayer *bgLayer = [BackgroundLayer layer];
	MainSplash *scene =  [MainSplash node];
	//[scene addChild: layer];
	
	
	
	
	
	// return the scene
	return scene;
}
-(id) init
{
	if( (self=[super init])) {
		
		
		CGSize screenSize = [CCDirector sharedDirector].winSize;
		CCLOG(@"Screen width in mainSplash %0.2f screen height %0.2f",screenSize.width,screenSize.height);
		
		//Set up sprite
		
		//CCSpriteSheet *ballsheet = [CCSpriteSheet spriteSheetWithFile:@"beetle_64_64.png" capacity:140];
		//[self addChild:ballsheet z:0 tag:kTagSpriteSheetBall];
		
		//CCSprite *sprite = [CCSprite spriteWithFile:@"splash_mockup.png"];
		CCSprite *sprite = [CCSprite spriteWithFile:@"splash_test.png"];
		[self addChild:sprite];
		sprite.position = ccp( screenSize.width/2, screenSize.height/2);
		
		/*
		NSDictionary* settings = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithBool:YES],OpenFeintSettingDisableUserGeneratedContent,
																			[NSNumber numberWithBool:YES],OpenFeintSettingPromptToPostAchievementUnlock,
																			[NSNumber numberWithInt:UIInterfaceOrientationLandscapeRight],OpenFeintSettingDashboardOrientation,
																			[NSNumber numberWithBool:YES],OpenFeintSettingGameCenterEnabled,
																			nil];
		ofDelegate = [SampleOFDelegate new];
		
		[ofDelegate setMainSplash:self];
		OFDelegatesContainer* delegates = [OFDelegatesContainer containerWithOpenFeintDelegate:ofDelegate];
		
		[OpenFeint initializeWithProductKey:@"cigckqlG3ipE7dSVhC4g"
								  andSecret:@"qOorJ9RTZxduyt1raIVPZ10TD7QFEMI32Wkl7SAdo0"
							 andDisplayName:@"Monkey Swipe"
								andSettings:settings    // see OpenFeintSettings.h
							   andDelegates:delegates]; // see OFDelegatesContainer.h
		//orientation in spearate call fixing OF 2.6 glitchy init on new devices. 
		//[OpenFeint setDashboardOrientation:UIInterfaceOrientationLandscapeRight]; 
		//[OpenFeint setDashboardOrientation:[NSNumber numberWithInt:UIInterfaceOrientationLandscapeRight]];  
		*/
        /*
		 
		 83734
		 Product Key
		 cigckqlG3ipE7dSVhC4g
		 Product Secret
		 qOorJ9RTZxduyt1raIVPZ10TD7QFEMI32Wkl7SAdo0
		 
		 */
		
        
        [self authenticateLocalPlayer];
		
		
		
		
		[[SimpleAudioEngine sharedEngine] preloadEffect:@"btnTap.wav"];
		[[SimpleAudioEngine sharedEngine] preloadEffect:@"switch.wav"];
		
		[SimpleAudioEngine sharedEngine].muted = YES; //buggur!!!!!!!!!
		//reading from Documents path
		NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
		NSString *documentsDirectory = [paths objectAtIndex:0];
		NSString *appSettingsPath = [documentsDirectory stringByAppendingPathComponent:@"settings.plist"];
		NSMutableDictionary *settings2 = [NSMutableDictionary dictionaryWithContentsOfFile:appSettingsPath];
		[[OOOGameSettingsManager sharedManager] setSettings:settings2];
		/*
		//reading sound config file in bundle
		NSString *file = [[NSBundle mainBundle] pathForResource:@"settings" ofType:@"plist"];
		
		NSMutableDictionary *settings2 = [NSMutableDictionary dictionaryWithContentsOfFile:file];
		*/
		//NSLog(@"%@",settings2);
		BOOL soundFXMuted = [[settings2 objectForKey:@"soundFXMuted"] boolValue];
		//NSLog(@" dit is de nsnumber value: %p",soundFXMuted);
		
		if(soundFXMuted != YES){
			[SimpleAudioEngine sharedEngine].muted = soundFXMuted;
		}
		//NSLog(@"-- %@",[SimpleAudioEngine sharedEngine]);
		//start some sequence
		
	}
	return self;
}	


+(BOOL) isGameCenterAPIAvailable
{
    // Check for presence of GKLocalPlayer class.
    BOOL localPlayerClassAvailable = (NSClassFromString(@"GKLocalPlayer")) != nil;
    
    // The device must be running iOS 4.1 or later.
    NSString *reqSysVer = @"4.1";
    NSString *currSysVer = [[UIDevice currentDevice] systemVersion];
    BOOL osVersionSupported = ([currSysVer compare:reqSysVer options:NSNumericSearch] != NSOrderedAscending);
    
   // NSMutableDictionary *settings = [[OOOGameSettingsManager sharedManager] getSettings];
    BOOL useGameCenter = YES; //[[settings objectForKey:@"useGameCenter"] boolValue];
    NSLog(@"isGamecenterAPI??? %i",osVersionSupported );
    return (localPlayerClassAvailable && osVersionSupported && useGameCenter);
    
}



- (void) authenticateLocalPlayer
{
    
    //OOOGameSettingsManager *sm = [OOOGameSettingsManager sharedManager];
    //NSMutableDictionary *settings = [sm getSettings];
   
    
    
    if(![MainSplash isGameCenterAPIAvailable]){
        return;
    };
    NSLog(@"authenticateLocalPlayer :"); 
    GKLocalPlayer *localPlayer = [GKLocalPlayer localPlayer];
    [localPlayer authenticateWithCompletionHandler:^(NSError *error) {
        if(error != nil){
            NSLog(@"error! %@",[error localizedDescription]);
            NSLog(@"error! %@",[error localizedRecoverySuggestion ]);
        }
        if (localPlayer.isAuthenticated)
        {
            NSLog(@"authenticated");
        }else{
            NSLog(@"Not authenticated!");
        }
        
        //[[NSNotificationCenter defaultCenter]
        // postNotification:[NSNotification
        //                   notificationWithName:@"resumeGame"
        //                   object:nil
        //                   userInfo:nil]];
        
    }];
}





-(void) go
{
	[[SimpleAudioEngine sharedEngine] playEffect:@"sfx_monkey_swipe_combined2.wav"];
	///hovering caterpillar
	CCSprite *titleSpr = [CCSprite spriteWithFile:@"monkey_swipe_title.png"];
	//[self addChild:titleSpr];
	CCSprite *loaderbarContainer = [CCSprite spriteWithFile:@"loaderbarContainer.png"];
	CCSprite *loaderbar = [CCSprite spriteWithFile:@"loaderbar.png"];
	[self addChild:loaderbarContainer];
	[self addChild:loaderbar];
	
	
	CGFloat loaderbarWidth = loaderbar.contentSize.width;
	loaderbar.scaleX = .01f;
	//loaderbar.position=ccp(240.0f - loaderbarWidth/2, 40.0f);
	//loaderbarContainer.position=ccp(240.0f, 40.0f);	
	loaderbar.position=ccp(240.0f - loaderbarWidth/2, 80.0f);
	loaderbarContainer.position=ccp(240.0f, 80.0f);	
	titleSpr.position=ccp(240.0f, 240.0f);
	
	
	
	id move_action = [CCMoveBy actionWithDuration:1 position:ccp(0.0f,10.0f)];
	id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
	id easeBack_action = [ease_action reverse];
	id seq = [CCSequence actions:ease_action, easeBack_action, nil];
	[titleSpr runAction:[CCRepeatForever actionWithAction:seq]];
		
	//id fadeOut_action = [CCFadeOut actionWithDuration:3 ];
	//id ease_alpha_action = [CCEaseInOut actionWithAction:fadeOut_action rate:2];
	//id easeBack_alpha_action = [ease_alpha_action reverse];
	//id alphaseq = [CCSequence actions:ease_alpha_action, easeBack_alpha_action, nil];
	//[dropshadowSpr runAction:[CCRepeatForever actionWithAction:alphaseq]];
	
	id functioncall_action = [CCCallFunc actionWithTarget:self selector:@selector(goMenu:)];
	id seq2 = [CCSequence actions:[CCDelayTime actionWithDuration: 2.0f],functioncall_action,nil]; 
    
	id loadProgress = [CCScaleTo actionWithDuration:1.0f scaleX:1.0f scaleY:1.0f];
	id ease_action2 = [CCEaseIn actionWithAction:loadProgress rate:2];
	[loaderbar runAction:ease_action2];
	
	id loadProgress2 = [CCMoveBy actionWithDuration:1.0f position:ccp(loaderbarWidth/2,0.0f)];
	id ease_action3 = [CCEaseIn actionWithAction:loadProgress2 rate:2];
	[loaderbar runAction:ease_action3];
	
	[self runAction:seq2];
	//[self goMenu];
}

/*
- (void) onExit{
	[super onExit];
}
*/
-(void) goMenu:(id)sender
{
	//NSLog(@"goMEnu called");
		//[[CCDirector sharedDirector] runWithScene: [MainMenu scene]];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];

}



- (void)dealloc {
	//NSLog(@"deallocing mainsplash");
    [super dealloc];
}


@end
