#pragma once

#import "OpenFeintDelegate.h"
#import "MainSplash.h";

@interface SampleOFDelegate : NSObject< OpenFeintDelegate >
{
	MainSplash *mainSplash;
}


- (void)dashboardWillAppear;
- (void)dashboardDidAppear;
- (void)dashboardWillDisappear;
- (void)dashboardDidDisappear;
- (void)userLoggedIn:(NSString*)userId;
- (void)setMainSplash:(MainSplash*) __mainSplash;
- (BOOL)showCustomOpenFeintApprovalScreen;

@end