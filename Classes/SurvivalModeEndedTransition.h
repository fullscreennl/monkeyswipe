//
//  SurvivalModeEndedTransition.h
//  MonkeySwipe
//
//  Created by Johan ten Broeke on 4/5/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "cocos2d.h"


@interface SurvivalModeEndedTransition :CCLayer {
	NSString *bgImage;
}
+(id) scene;
-(void) drawUI;
-(void) retry;
-(void) goMenu;
@end
