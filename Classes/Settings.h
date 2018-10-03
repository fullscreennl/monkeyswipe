//
//  MainSplash.h
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 fullscreen. All rights reserved.
//
#import "MainMenu.h"
#import <UIKit/UIKit.h>
#import "cocos2d.h"



@interface Settings : CCLayer {
	BOOL soundFXMuted;
	BOOL doodleStyle;
	CCSprite *swirlSprite;
	CCSprite *swirlSprite2;
	CCSprite *friendloudSpr; 
	CCSprite *friendSilentSpr; 
	CCSprite *friendDoodleloudSpr;
	CCSprite *friendDoodleSilentSpr;
	NSMutableDictionary * settings; 
}

+(id) scene;

-(id) init;
-(void)setSwirlPos:(BOOL)_soundState;
-(void)toggleSound;
-(void)toggleDoodle;
@end