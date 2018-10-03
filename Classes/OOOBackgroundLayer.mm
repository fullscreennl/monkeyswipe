//
//  OOOBackgroundLayer.mm
//  oneonone
//
//  Created by Johan ten Broeke on 2/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "OOOBackgroundLayer.h"


@implementation OOOBackgroundLayer

+(id) layer
{
	OOOBackgroundLayer *layer = [OOOBackgroundLayer node];
	return layer;
}

// initialize your instance here
-(id) init
{
	if( (self=[super init])) {
		self.isTouchEnabled = NO;
	}
	return self;
}


// on "dealloc" you need to release all your retained objects
- (void) dealloc
{
	//NSLog(@"backgroundlayer dealloced!!");
	[super dealloc];
}
@end


