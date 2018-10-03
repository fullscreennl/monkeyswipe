//
//  OOOBackgroundLayer.h
//  oneonone
//
//  Created by Johan ten Broeke on 2/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "cocos2d.h"
#import "GLES-Render.h"

// bg Layer
@interface OOOBackgroundLayer : CCLayer
{
	CCSprite* bgsprite;
}



// adds a new sprite at a given coordinate

+(id) layer; 
@end
