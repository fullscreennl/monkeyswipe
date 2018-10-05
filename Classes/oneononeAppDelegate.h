//
//  oneononeAppDelegate.h
//  oneonone
//
//  Created by Johan ten Broeke on 2/20/10.
//  Copyright fullscreen.nl 2010. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "OOOGameModel.h"
#import <GameKit/GameKit.h>

@interface oneononeAppDelegate : NSObject <UIApplicationDelegate, GKLeaderboardViewControllerDelegate, UIAlertViewDelegate> {
	UIWindow *window;
	BOOL level_done;
	NSString *currentLevelId;
	NSMutableData *receivedData;
	NSDictionary *daily_level_dict; 
	NSString *last_played_level_id;
    UIViewController *controller;
    int screenWidth;
    int screenHeight;
}

@property (nonatomic, retain) UIWindow *window;

-(void) onWin:(NSNotification *) note;
-(void) onLose:(NSNotification *) note;
-(void) levelDone:(BOOL)done;
-(void) onReturnToMainMenu:(NSNotification *) note;
-(void) showAlert:(NSString *)msg;
-(void) alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex;
-(int) getDayNumber;
-(void)showLeaderboard:(NSNotification*)note;
-(void) authenticateLocalPlayer;
-(CGSize)getScreenSize;
-(CGPoint)getScreenCenter;
@end
