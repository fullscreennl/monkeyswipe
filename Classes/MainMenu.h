//
//  MainSplash.h
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//
#import "MainMenu.h"
#import <UIKit/UIKit.h>
#import "cocos2d.h"

//@class SampleOFDelegate; // Add for OpenFeint

@interface MainMenu : CCScene {
	//SampleOFDelegate *ofDelegate; // Add for OpenFeint
	UIActivityIndicatorView *ai;
	BOOL busyUpgrading;
	
	NSMutableArray *map_ids;
}

-(void) showActivityIndicator;
-(void) hideActivityIndicator;
-(void)onUpgradeFailed:(NSNotification *) note;

+(id) scene;

-(id) init;
-(void) goSettings: (id)sender;
-(void) goTutorial: (id)sender;
-(void) goPlay: (id)sender;
-(void) goScores:(id)sender;
-(void) goCredits:(id)sender;
-(void) goSurvival: (id)sender;
-(void) resetObservers;

@end