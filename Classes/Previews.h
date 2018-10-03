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
#import "OOOLevelManager.h"


@interface Previews : CCScene {
	uint previewIndex;
	int maxlevels;
	CCMenuItem *prevBTN;
	CCMenuItem *nextBTN;
	CCMenuItem *playBTN;
	NSArray *previews;
	OOOLevelManager *levelManager;
	uint currentLevel;
}

+(id) scene;
-(id) init;
-(void) buildPreviewWithIndex: (uint) pIndex;
@end