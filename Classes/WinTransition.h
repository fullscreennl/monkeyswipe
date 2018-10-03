//
//  WinTransition.h
//  oneonone
//
//  Created by johan ten broeke on 3/22/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "cocos2d.h"

@interface WinTransition : CCLayer {
	NSString *bgImage;
}
+(id) scene;
-(void) goNextLevel;
-(void) goMenu;
-(void) drawUI;
@end
