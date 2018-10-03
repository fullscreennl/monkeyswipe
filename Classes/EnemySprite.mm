//
//  EnemySprite.m
//  oneonone
//
//  Created by Johan ten Broeke on 3/5/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "EnemySprite.h"


@implementation EnemySprite

-(id)init{
	if( (self=[super init])) {
		[self createKeyFrames];
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onLevelLoaded:) 
													 name:@"levelLoaded" 
												   object:nil];
	}
	//[self obeyPhysics:NO];
	return self;
}


-(void) onLevelLoaded:(NSNotification *) note{
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onWin:) 
												 name:@"onWin" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onLose:) 
												 name:@"onLose" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onDestroy:) 
												 name:@"onDestroy" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onReleaseStar:) 
												 name:@"onReleaseStar" 
											   object:nil];


}

-(void)didFinishEatAnimation: (id)sel{
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onRetryTransition" 
					   object:nil
					   userInfo:nil]];
}


-(void) createKeyFrames{
	NSMutableArray *animFrames = [NSMutableArray array];
	for(int i = 1; i <= 8; i++) {
		[animFrames addObject:[NSString stringWithFormat:@"enemy%04d.png",i]];
	}
	[self setKeyFrames:animFrames];
}

-(void) onReleaseStar:(NSNotification *) note{
	[self destroyJointByName:@"star_joint"];	
}


-(void) onDestroy:(NSNotification *) note{
	//[(CPPProxy*)[note object] getObject]->deactivate();
	if([[note userInfo] objectForKey:@"sprite1"]==self or [[note userInfo] objectForKey:@"sprite2"]==self){
		//NSLog(@"onDestroy %@",self);
		[[NSNotificationCenter defaultCenter] removeObserver:self];	
		[self destroyPhysics];
		[self playFrames:[NSArray arrayWithObjects:@"clouds0001.png",@"clouds0002.png",@"clouds0003.png",
					  @"clouds0004.png",nil] loop:NO target:self callback:@selector(clear:)];
	}
	
}

-(void)clear: (id)sel{
	//NSLog(@"callbak!!!");
	[[self parent] removeChild:self cleanup:NO];
}


-(void) onLose:(NSNotification *) note{
	[[NSNotificationCenter defaultCenter] removeObserver:self];	
	if([[note userInfo] objectForKey:@"sprite1"]==self or [[note userInfo] objectForKey:@"sprite2"]==self){
		[self gotoAndPlay:@"enemy0001.png" target:self callback:@selector(didFinishEatAnimation:)];
	}
}

-(void) onWin:(NSNotification *) note{

	//NSLog(@"onWin %@",self);
	[[NSNotificationCenter defaultCenter] removeObserver:self];	

	[self destroyPhysics];
	[self playFrames:[NSArray arrayWithObjects:@"clouds0001.png",@"clouds0002.png",@"clouds0003.png",
					  @"clouds0004.png",nil] loop:NO target:self callback:@selector(clear:)];
	
	
}

- (void) dealloc
{
	[[NSNotificationCenter defaultCenter] removeObserver:self]; 
	[super dealloc];
}



@end
