//
//  NutSprite.m
//  oneonone
//
//  Created by johan ten broeke on 3/10/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "SpikeySprite.h"
#import "SimpleAudioEngine.h"

@implementation SpikeySprite



-(id)init{
	if( (self=[super init])) {
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onLevelLoaded:) 
													 name:@"levelLoaded" 
												   object:nil];
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onDestroy:) 
													 name:@"onDestroy" 
												   object:nil];
	}
	playing = YES;
	return self;
	
}


-(void) onLevelLoaded:(NSNotification *) note{
	//[self playFrames:[NSArray arrayWithObjects:@"spikey_buddy0001.png",@"spikey_buddy0002.png",nil] loop:YES target:self callback:@selector(clear:)];
}

-(void) onDestroy:(NSNotification *) note{
	//[(CPPProxy*)[note object] getObject]->deactivate();
	if([[note userInfo] objectForKey:@"sprite1"]==self or [[note userInfo] objectForKey:@"sprite2"]==self){
		//NSLog(@"onDestroy %@",self);
		[[SimpleAudioEngine sharedEngine] playEffect:@"sfx_hmm_gotcha.wav"];
	}
	
}

-(void)update{
	if (_obeyPhysics) {
		self.position = CGPointMake( myBody->GetPosition().x * PTM_RATIO, myBody->GetPosition().y * PTM_RATIO);
		float xspeed = abs(myBody->GetLinearVelocity().x * PTM_RATIO);
		if (xspeed < 2.0f and playing == YES){
			playing = NO;
			[self stopAllActions];
		}else if(xspeed >= 2.0f and playing == NO){
			playing = YES;
			[self playFrames:[NSArray arrayWithObjects:@"spikey_buddy0001.png",@"spikey_buddy0002.png",nil] loop:YES target:nil callback:nil];
		}

	}
}

- (void) dealloc
{
	[[NSNotificationCenter defaultCenter] removeObserver:self]; 
	[super dealloc];
}

@end
