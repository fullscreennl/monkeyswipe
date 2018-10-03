//
//  LevelPackMenu.h
//  MonkeySwipe
//
//  Created by Johan ten Broeke on 5/22/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "MainMenu.h"
#import <UIKit/UIKit.h>
#import "cocos2d.h"


@interface LevelPackMenu : CCScene {
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

@end
