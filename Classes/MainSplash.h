//
//  MainSplash.h
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//
#import "MainSplash.h"
#import <UIKit/UIKit.h>
#import "cocos2d.h"

@class SampleOFDelegate; // Add for OpenFeint

@interface MainSplash : CCScene {
	//SampleOFDelegate *ofDelegate; // Add for OpenFeint
}
+(id) scene;

-(id) init;
-(void) goMenu:(id)sender;
-(void) go;
+(BOOL) isGameCenterAPIAvailable;
- (void) authenticateLocalPlayer;
@end