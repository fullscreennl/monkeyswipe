//
//  oneononeAppDelegate.m
//  oneonone
//
//  Created by Johan ten Broeke on 2/20/10.
//  Copyright fullscreen.nl 2010. All rights reserved.
//

#define SWIPE_MASTER @"278144"

#import "oneononeAppDelegate.h"
#import "cocos2d.h"
#import "OOOGameView.h"
#import "OOONotificationNames.h"
#import "OOOLevelMap.h"
#import "MainSplash.h"
#import "LoseTransition.h"
#import "WinTransition.h"
#import "SimpleAudioEngine.h"
#import <AudioToolbox/AudioToolbox.h>
#import "UpgradeTransition.h"
#import "SurvivalModeEndedTransition.h"
#import "FinalTransition.h"
#import "MainMenu.h"
#import <UIKit/UIKit.h>
#import "DailySwipeEndedTransition.h"
#import "RandomSwipeEndedTransition.h"
#import "Appirater.h"


@implementation oneononeAppDelegate

@synthesize window;

- (void) applicationDidFinishLaunching:(UIApplication*)application
{
	
	// Init the window
	window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
	[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(showLeaderboard:) name:@"showLeaderboard" object:nil];
	// cocos2d will inherit these values
	[window setUserInteractionEnabled:YES];	
	[window setMultipleTouchEnabled:YES];
	[self levelDone:NO];
	
	// Try to use CADisplayLink director
	// if it fails (SDK < 3.1) use the default director
	if( ! [CCDirector setDirectorType:CCDirectorTypeDisplayLink] )
		[CCDirector setDirectorType:CCDirectorTypeDefault];
	
	// Use RGBA_8888 buffers
	// Default is: RGB_565 buffers
	[[CCDirector sharedDirector] setPixelFormat:kPixelFormatRGBA8888];
	
	// Create a depth buffer of 16 bits
	// Enable it if you are going to use 3D transitions or 3d objects
//	[[CCDirector sharedDirector] setDepthBufferFormat:kDepthBuffer16];
	
	// Default texture format for PNG/BMP/TIFF/JPEG/GIF images
	// It can be RGBA8888, RGBA4444, RGB5_A1, RGB565
	// You can change anytime.
	[CCTexture2D setDefaultAlphaPixelFormat:kTexture2DPixelFormat_RGBA8888];
	
	// before creating any layer, set the landscape mode
	[[CCDirector sharedDirector] setDeviceOrientation:CCDeviceOrientationLandscapeLeft];
	[[CCDirector sharedDirector] setAnimationInterval:1.0/60];
	//[[CCDirector sharedDirector] setDisplayFPS:YES];
	
	// create an openGL view inside a window
	[[CCDirector sharedDirector] attachInView:window];	
	controller = [[UIViewController alloc] init];
    
    [controller.view setUserInteractionEnabled:NO];
    [window makeKeyAndVisible];
	   
	//gameModel = [[[OOOGameModel alloc] init] retain];
		
	MainSplash	*mainSplash = [MainSplash scene];
	
	[[CCDirector sharedDirector] runWithScene: (CCScene*) mainSplash];
	[mainSplash go];
	
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onWin:) 
												 name:@"onWin" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onLose:) 
												 name:@"onLose" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onLevelLoaded:) 
												 name:@"levelLoaded" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(levelEntered:) 
												 name:@"levelEntered" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(goBack:) 
												 name:@"goBack" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onRetryTransition:) 
												 name:@"onRetryTransition" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(reloadLevel:) 
												 name:@"reloadLevel" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onTutorialFinished:) 
												 name:@"onTutorialFinished" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onTutorialsDone:) 
												 name:@"onTutorialsDone" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(goBack:) 
												 name:@"onLeaveLevel" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onSurvivalModeEntered:) 
												 name:@"onSurvivalModeEntered" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onReturnToMainMenu:) 
												 name:@"onReturnToMainMenu" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onUpgradeRequested:) 
												 name:@"onUpgradeRequested" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(loadDailyLevel:) 
												 name:@"onDailyLevel" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(loadRandomLevel:) 
												 name:@"onRandomLevel" 
											   object:nil];

	[[SimpleAudioEngine sharedEngine] preloadEffect:@"eat_edit.wav"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"okay_edit.wav"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"sfx_enemy_bounce_a.wav"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"sfx_enemy_bounce_b.wav"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"sfx_small_explosion.wav"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"sfx_bomb_sound.wav"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"sfx_hmm_gotcha.wav"];
	
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"suspence_1.mp3"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"suspence_2.mp3"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"suspence_3.mp3"];
	[[SimpleAudioEngine sharedEngine] preloadEffect:@"lose_chord.mp3"];
	
	[[SimpleAudioEngine sharedEngine] playBackgroundMusic:@"bg_music.mp3" loop:YES];
	
	[CCBitmapFontAtlas bitmapFontAtlasWithString:@"Loading!" fntFile:@"marker_felt2.fnt"];
	
	[Appirater appLaunched];

}

-(void)showLeaderboard:(NSNotification*)note{
    
    if(![MainSplash isGameCenterAPIAvailable]){
        return;
    };
    
    GKLocalPlayer *localPlayer = [GKLocalPlayer localPlayer];
    if(localPlayer.authenticated){
        NSLog(@"showleaderboard!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
        [window setRootViewController:controller];
        GKLeaderboardViewController *lb = [[GKLeaderboardViewController alloc] init];
        if(lb != nil){
            lb.leaderboardDelegate = self;
            NSLog(@"window.rootViewController %@",window.rootViewController);
            [window.rootViewController presentModalViewController:lb animated:YES];
        }
    }else{
        UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"No highscores!" message:@"You can still join GameCenter!" delegate:self cancelButtonTitle:@"No thanks" otherButtonTitles:@"Yes please", nil];
        [alert show];
        [alert release];
    }
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

-(void)alertView:(UIAlertView *)alertView didDismissWithButtonIndex:(NSInteger)buttonIndex{
    NSLog(@"btnindex:%i",buttonIndex);
    if(buttonIndex==0){
        return;
    }else if(buttonIndex==1){
        [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"gamecenter:"]];
    }
}

- (void)leaderboardViewControllerDidFinish:(GKLeaderboardViewController *)viewController
{
    [window.rootViewController dismissModalViewControllerAnimated: YES];
    [window setRootViewController:nil];
    [viewController release];
}


-(void)onLevelLoaded:(NSNotification *) note{
	[self levelDone:NO];
}

-(void)levelDone:(BOOL)done{
	level_done = done;
}

-(void)goBack:(NSNotification *) note{
	[self levelDone:YES];
	[[OOOLevelManager sharedLevelManager] clearScore];
	[[SimpleAudioEngine sharedEngine] resumeBackgroundMusic];
	if ([[OOOLevelManager sharedLevelManager] isSurvival] or [[OOOLevelManager sharedLevelManager] isDaily] or [[OOOLevelManager sharedLevelManager] isRandom]){
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];
	}else{
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[OOOLevelMap scene]]];
	}
}

-(void)levelEntered:(NSNotification *) note{
	int level_ind = [[[note userInfo] objectForKey:@"level_ind"] intValue];
	BOOL has_tutorial = [[[note userInfo] objectForKey:@"tutorial"] boolValue];
	if (level_ind < 1 && has_tutorial){
		[[OOOLevelManager sharedLevelManager] enterTutorialMode];
	}else{
		[[OOOLevelManager sharedLevelManager] enterGameMode];
	}
	[[OOOLevelManager sharedLevelManager] setCurrentLevelIndex:level_ind];

	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.01 scene:[LoseTransition scene]]];
}

-(void)onSurvivalModeEntered:(NSNotification *) note{
	[[OOOLevelManager sharedLevelManager] enterSurvivalMode];
	[[OOOLevelManager sharedLevelManager] setCurrentLevelIndex:1];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.01 scene:[LoseTransition scene]]];
}

-(void) onTutorialFinished:(NSNotification *) note{
	if (!level_done){
		[self levelDone:YES];
		[[OOOLevelManager sharedLevelManager] unlockNextTutorial];
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[LoseTransition scene]]];
		[[SimpleAudioEngine sharedEngine] playEffect:@"okay_edit.wav"];
	}
}

-(void) onReturnToMainMenu:(NSNotification *) note{
	[[SimpleAudioEngine sharedEngine] resumeBackgroundMusic];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];
}

-(void) onTutorialsDone:(NSNotification *) note{
	if (!level_done){
		[self levelDone:YES];
		[[OOOLevelManager sharedLevelManager] enterGameMode];
		[[OOOLevelManager sharedLevelManager] unlockNextLevel];
		[[OOOLevelManager sharedLevelManager] incrementLevel];
		[[OOOLevelManager sharedLevelManager] clearScore];
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[LoseTransition scene]]];
		[[SimpleAudioEngine sharedEngine] playEffect:@"okay_edit.wav"];
	}
}


-(void) onWin:(NSNotification *) note{
	if (! level_done) {
		[self levelDone:YES];
		[[SimpleAudioEngine sharedEngine] playEffect:@"jippie2.mp3"];
		//[[SimpleAudioEngine sharedEngine] playEffect:@"suspence_3.mp3"];
		if ([[OOOLevelManager sharedLevelManager] isDaily] ){
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[DailySwipeEndedTransition scene]]];
		}else if([[OOOLevelManager sharedLevelManager] isRandom] ){
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[RandomSwipeEndedTransition scene]]];
		}else if ([[OOOLevelManager sharedLevelManager] isSurvival]){
			[[OOOLevelManager sharedLevelManager] progressSurvival];
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[LoseTransition scene]]];
		}else{
			currentLevelId = [[OOOLevelManager sharedLevelManager] currentLevelID];
			[[OOOLevelManager sharedLevelManager] commitScore];
			[[OOOLevelManager sharedLevelManager] unlockNextLevel];
			int currentLevelIndex = [[OOOLevelManager sharedLevelManager] getCurrentLevelIndex];
			//NSLog(@"level index %i",currentLevelIndex);
			if(currentLevelIndex == 39){
				[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[FinalTransition scene]]];
			}else if (currentLevelIndex >= 9 and [[OOOLevelManager sharedLevelManager] hasUpgraded] == NO){
				[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[UpgradeTransition scene]]];
			}else{
				[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[WinTransition scene]]];
			}
			[[OOOLevelManager sharedLevelManager] save];
		}	
	}
}

-(void)onUpgradeRequested:(NSNotification *) note{
	[[OOOLevelManager sharedLevelManager] explicitUpgrade];
}

-(void) onLose:(NSNotification *) note{
	[[SimpleAudioEngine sharedEngine] playEffect:@"lose_chord.mp3"];
	if ([[OOOLevelManager sharedLevelManager] isSurvival] and !level_done){
		[self levelDone:YES];
		//[[OOOLevelManager sharedLevelManager] calcSurvivalScore];
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1 scene:[SurvivalModeEndedTransition scene]]];
	}else if (!level_done){
		[self levelDone:YES];
		[[OOOLevelManager sharedLevelManager] clearScore];
		[[SimpleAudioEngine sharedEngine] playEffect:@"eat_edit.wav"];
	}
}

-(void)reloadLevel:(NSNotification *) note{
	//NSLog(@"level_id in reloadlevel before assigning");
	[[SimpleAudioEngine sharedEngine] pauseBackgroundMusic];
	if ([[OOOLevelManager sharedLevelManager] isDaily]){
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.2 scene:[OOOGameView sceneWithDictionary:daily_level_dict]]];
	}else{
		NSString *level_id = [[OOOLevelManager sharedLevelManager] currentLevelID];
		//NSLog(@"level_id in reloadlevel: %@",level_id);
		if (last_played_level_id != level_id) {
			[[SimpleAudioEngine sharedEngine] playEffect:@"lose_chord.mp3"];
		}
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.2 scene:[OOOGameView sceneWithLevelId:level_id]]];
		last_played_level_id = level_id;
	}
}

//////////////////////////////////
// ***** LOAD DAILY LEVEL ******//
//////////////////////////////////

-(void)showAlert:(NSString *)msg{
	UIAlertView *myAlert = [[UIAlertView alloc] initWithTitle:@"Oops!"
												   message:msg
												  delegate:self
										 cancelButtonTitle:@"OK"
										 otherButtonTitles:nil];
	[myAlert show];
    [myAlert release];
}

//- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex{
//	[alertView release];
//}

-(int)getDayNumber{
	NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
	int dayOfYear = [gregorian ordinalityOfUnit:NSDayCalendarUnit inUnit:NSYearCalendarUnit forDate:[NSDate date]];
	[gregorian release];
	return dayOfYear;
}

-(void)loadDailyLevel:(NSNotification *) note{
	
	[[SimpleAudioEngine sharedEngine] pauseBackgroundMusic];

	NSString *uri = @"http://www.fullscreen.nl/monkeyswipe_app/daily.php?d=";
	//NSString *uri = @"http://www.fullscreen.nl/monkeyswipe_app/daily_swipe_staging.php?d=";
	NSString *daynum = [[NSNumber numberWithInt:[self getDayNumber]]stringValue];
	NSString *daily_level = [uri stringByAppendingString:daynum];
	NSURL *url = [NSURL URLWithString:daily_level];
	NSURLRequest *theRequest=[NSURLRequest requestWithURL:url
											  cachePolicy:NSURLRequestUseProtocolCachePolicy
										  timeoutInterval:60.0];

	[[OOOLevelManager sharedLevelManager] setDayNumber:daynum];
	
	NSURLConnection *theConnection=[[NSURLConnection alloc] initWithRequest:theRequest delegate:self];
	
	if (theConnection) {
		//NSLog(@"loading started !");
		receivedData = [[NSMutableData data] retain];
		
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"loadingDailySwipe" 
						   object:nil 
						   userInfo:nil]];
		
	} else {
		//NSLog(@"no data !");
	}
}


-(void)loadRandomLevel:(NSNotification *) note{
	if([[OOOLevelManager sharedLevelManager] hasUpgraded] == YES){
		[[SimpleAudioEngine sharedEngine] pauseBackgroundMusic];
		[[OOOLevelManager sharedLevelManager] enterRandomMode];
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.01 scene:[LoseTransition scene]]];
		//[self reloadLevel:nil];
	}
}
	

- (void)connection:(NSURLConnection *)connection didReceiveResponse:(NSURLResponse *)response
{
	[receivedData setLength:0];
}

- (void)connection:(NSURLConnection *)connection didReceiveData:(NSData *)data
{
	[receivedData appendData:data];	
}

- (void)connection:(NSURLConnection *)connection
  didFailWithError:(NSError *)error
{

    [connection release];
	[receivedData release];

    //NSLog(@"Connection failed! Error - %@ %@",
    //      [error localizedDescription],
    //      [[error userInfo] objectForKey:NSErrorFailingURLStringKey]);
	
	[self showAlert: @"To play the Daily Swipe an internet connection is required."];
	
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"loadingDailySwipeDone" 
					   object:nil 
					   userInfo:nil]];
	
	
}

- (void)connectionDidFinishLoading:(NSURLConnection *)connection
{
	

	NSString *level_loading_error = @"error loading level";
	NSPropertyListFormat format = NSPropertyListXMLFormat_v1_0;  

	[daily_level_dict release];
	daily_level_dict = [NSPropertyListSerialization propertyListFromData:receivedData 
																mutabilityOption:NSPropertyListImmutable 
																		  format:&format 
																errorDescription:&level_loading_error];
	
	//NSLog(@"leveldict :%@ ",daily_level_dict);
	
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"loadingDailySwipeDone" 
					   object:nil 
					   userInfo:nil]];
	
	[daily_level_dict retain];

	if(daily_level_dict){
		[[OOOLevelManager sharedLevelManager] enterDailyMode];
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.5 scene:[OOOGameView sceneWithDictionary:daily_level_dict]]];
	}else {
		[self showAlert:@"Error loading the daily Swipe!"];
	}

	[receivedData release];
    [connection release];
}

//////////////////////////////////
// ***** END DAILY LEVEL  ******//
//////////////////////////////////


-(void)onRetryTransition:(NSNotification *) note{
	if (![[OOOLevelManager sharedLevelManager] isSurvival]){
		[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:0.2 scene:[LoseTransition scene]]];
	}
}

- (void)applicationWillResignActive:(UIApplication *)application {
	[[CCDirector sharedDirector] pause];
}

- (void)applicationDidBecomeActive:(UIApplication *)application {
	[[CCDirector sharedDirector] resume];
}

- (void)applicationDidReceiveMemoryWarning:(UIApplication *)application {
	[[CCTextureCache sharedTextureCache] removeUnusedTextures];
}

- (void)applicationWillTerminate:(UIApplication *)application {
	[[OOOLevelManager sharedLevelManager] save];
	[[CCDirector sharedDirector] end];
}

- (void)applicationSignificantTimeChange:(UIApplication *)application {
	[[CCDirector sharedDirector] setNextDeltaTimeZero:YES];
}

- (void)dealloc {
	[[CCDirector sharedDirector] release];
	[window release];
	[daily_level_dict release];
	[super dealloc];
}

@end
