//
//  OOOGameView.h
//  oneonone
//
//  Created by Johan ten Broeke on 2/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

// When you import this file, you import all the cocos2d classes
#import "cocos2d.h"
#import "OOOGameSprite.h"
#import "OOOGameModel.h"
#import "GLES-Render.h"
#import "OOOLevelData.h"
#import "OOOBackgroundLayer.h"
#import "OOODebugDrawLayer.h"
#import "OOOJointLayer.h"

@interface OOOGameView : CCLayer {
	OOOGameModel *gameModel;
	UITouch *currentTouch;
	CGPoint currentLocation;
	NSDictionary *level_data; 
	OOOBackgroundLayer *bgLayer;
	OOODebugDrawLayer *dbDrawLayer;
	OOOJointLayer *jointLayer;
	OOOLevelData *level_data_loader;
}
+(id) sceneWithLevelId:(NSString *)level_id;
+(id) sceneWithDictionary:(NSDictionary *)dict;
-(void) buildLevel:(NSString *)level_id;
-(void) drawCompounds;
-(void) buildSpriteSheets;
-(void) buildJoints;
-(void) drawBackground;
-(void) drawCompoundWithDict: (NSDictionary *)dict;
-(void) registerContacts;
-(void) createDebugDraw;
-(void) drawJointLayer;
-(void) enhanceBackground;
-(void) drawQuitButton;
-(void) drawQuitButton;
-(void) drawLevel;
-(void) buildLevelWithDictionary:(NSDictionary *)dict;
@end
