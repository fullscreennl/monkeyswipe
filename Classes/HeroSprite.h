//
//  HeroSprite.h
//  oneonone
//
//  Created by johan ten broeke on 3/12/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "OOOGameSprite.h"


@interface HeroSprite : OOOGameSprite {

}

-(void) onLevelLoaded:(NSNotification *) note;
-(void) onSwipe:(NSNotification *) note;

@end
