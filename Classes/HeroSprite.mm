//
//  HeroSprite.m
//  oneonone
//
//  Created by johan ten broeke on 3/12/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "HeroSprite.h"
#import "Box2D.h"
#import "oneononeAppDelegate.h"

@implementation HeroSprite

-(id)init{

	if( (self=[super init])) {
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onLevelLoaded:) 
													 name:@"levelLoaded" 
												   object:nil];
	}
	return self;
	
}


-(void) onLevelLoaded:(NSNotification *) note{
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onSwipe:) 
												 name:@"onSwipe" 
											   object:nil];
	/** Test for sub-shape collisions
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onRotorHit:) 
												 name:@"onRotorHit" 
											   object:nil];
	
	*/
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onLose:) 
												 name:@"onLose" 
											   object:nil];
	myBody->SetBullet(true);

}

-(void) onLose:(NSNotification *) note{
	[self destroyPhysics];
	[self playFrames:[NSArray arrayWithObjects:@"clouds0001.png",@"clouds0002.png",@"clouds0003.png",
					  @"clouds0004.png",nil] loop:NO target:self callback:@selector(clear:)];
}

-(void)clear: (id)sel{
	[[self parent] removeChild:self cleanup:NO];
}

/**
-(void) onRotorHit:(NSNotification *) note{
	if([[note userInfo] objectForKey:@"sprite1"]==self){
		NSLog(@"onRotorHit: %@",[[[note userInfo] objectForKey:@"sprite2"] getName]);
	}
	if ([[note userInfo] objectForKey:@"sprite2"]==self){
		NSLog(@"onRotorHit: %@",[[[note userInfo] objectForKey:@"sprite1"]getName]);
	}
}
*/

-(CGFloat)calcAspect:(CGSize)screensize{
    return screensize.width / screensize.height;
}

-(CGFloat)calculateDisplayMultiplier{
    CGSize oriSize = CGSizeMake(480,320);
    CGSize screenSize = [(oneononeAppDelegate*)[[UIApplication sharedApplication] delegate] getScreenSize];
    float factor = 1.0f;
    if ([self calcAspect:oriSize] > [self calcAspect:screenSize]){
        factor = screenSize.width / oriSize.width;
    }else{
        factor = screenSize.height / oriSize.height;
    }
    return factor;
}

-(void) onSwipe:(NSNotification *) note{
    float mp = [self calculateDisplayMultiplier];
	b2Vec2 point(myBody->GetPosition().x, myBody->GetPosition().y);
	b2Vec2 impulse(-[[[note userInfo] objectForKey:@"dx"] floatValue]*mp*mp,-[[[note userInfo] objectForKey:@"dy"] floatValue]*mp*mp);
    
	myBody->ApplyImpulse(impulse,point);	
}


- (void) dealloc
{
	[[NSNotificationCenter defaultCenter] removeObserver:self]; 
	[super dealloc];
}

@end
