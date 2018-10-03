//
//  OOOLevelMap.h
//  oneonone
//
//  Created by Johan ten Broeke on 3/2/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "cocos2d.h"
#import "OOOLevelManager.h"

@interface OOOLevelMap : CCLayer {
	OOOLevelManager *levelManager;
	CCLayer *menucont1;
	CCLayer *menucont2;
	CCMenu *subMenu;
	CCMenu *subMenu2;
	int pol;
	
	NSMutableArray *map_ids;
}
+(id) scene;
-(void) goSettings;
-(void) buildSubMenu;
-(void) goNextLevels;
-(void) goPreview;
@end

	