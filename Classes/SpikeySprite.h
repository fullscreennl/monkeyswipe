//
//  NutSprite.h
//  oneonone
//
//  Created by johan ten broeke on 3/10/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "OOOGameSprite.h"


@interface SpikeySprite : OOOGameSprite {
	BOOL playing;
}

-(void) onLevelLoaded:(NSNotification *) note;
@end
