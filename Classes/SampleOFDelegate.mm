#import "SampleOFDelegate.h"
#import "OpenFeint+UserOptions.h"
#import "cocos2d.h"

@implementation SampleOFDelegate

- (void)dashboardWillAppear
{
}

- (void)dashboardDidAppear
{
	[[CCDirector sharedDirector] pause];
	[[CCDirector sharedDirector] stopAnimation];
}

- (void)dashboardWillDisappear
{
}


-(void)setMainSplash:(MainSplash*) __mainSplash
{
	mainSplash = __mainSplash;
	//NSLog(@"setMAinSPlash: %@",mainSplash );
	
}

- (void)dashboardDidDisappear
{
	[[CCDirector sharedDirector] resume];
	[[CCDirector sharedDirector] startAnimation];
	//[mainSplash goMenu];
}

- (void)userLoggedIn:(NSString*)userId
{
	//OFLog(@"New user logged in! Hello %@", [OpenFeint lastLoggedInUserName]);
	//NSLog(@"user logged in");
	//[mainSplash goMenu];

}

- (BOOL)showCustomOpenFeintApprovalScreen
{
	return NO;
}

@end