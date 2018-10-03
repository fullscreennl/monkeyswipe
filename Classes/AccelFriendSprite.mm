//
//  NutSprite.m
//  oneonone
//
//  Created by johan ten broeke on 3/10/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "AccelFriendSprite.h"

@implementation AccelFriendSprite



-(id)init{
	if( (self=[super init])) {
				
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onAccel:) 
													 name:@"onAccel" 
												   object:nil];
		
	}
	return self;
	
}

-(void) onAccel:(NSNotification *) note{
	b2Vec2 point(myBody->GetPosition().x, myBody->GetPosition().y);
	//NSLog(@"userinfo %@",[note userInfo]);
	b2Vec2 impulse(-[[[note userInfo] objectForKey:@"dy"] floatValue] / 10.0 ,0);
	myBody->ApplyImpulse(impulse,point);	
}


- (void) dealloc
{
	[[NSNotificationCenter defaultCenter] removeObserver:self]; 
	[super dealloc];
}

@end
