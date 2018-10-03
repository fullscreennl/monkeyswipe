//
//  EnemySprite.h
//  oneonone
//
//  Created by Johan ten Broeke on 3/5/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "OOOGameSprite.h"


@interface EnemySprite :OOOGameSprite {
	CCAnimation *myKeyFrames;
}
-(void) createKeyFrames;

@end
