//
//  UpgradeTransition.m
//  MonkeySwipe
//
//  Created by johan ten broeke on 3/29/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "UpgradeTransition.h"
#import "OOOLevelManager.h"
#import "SimpleAudioEngine.h"



@implementation UpgradeTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	WinTransition *layer = [UpgradeTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		
		bgImage = @"upgrade_cutscene_bg.png";
		
		ai = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleWhiteLarge];
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(transactionFinished:) 
													 name:@"inAppPurchaseTransactionFailed" 
												   object:nil];
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(transactionFinished:) 
													 name:@"inAppPurchaseTransactionSuccess" 
												   object:nil];
		busyUpgrading = NO;
		
		[self drawUI];
	}
	return self;
}

-(void)transactionFinished: (NSNotification *)note{
	[self hideActivityIndicator];
	busyUpgrading = NO;
}

-(void) showActivityIndicator{
	[ai setHidden:NO];
	[ai startAnimating];
	[ai setCenter:CGPointMake(320-75, 75)];
	[[[CCDirector sharedDirector] openGLView]  addSubview:ai];
}

-(void) hideActivityIndicator{
	[ai removeFromSuperview];
}


- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	UITouch *touch = [touches anyObject];
	CGPoint location = [touch locationInView: [touch view]];
	//NSLog(@"touches pos: %3f",location.y);
	if (!busyUpgrading) {
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		if(location.y > 250.0f) {
				busyUpgrading = YES;
				BOOL success = [[OOOLevelManager sharedLevelManager] incrementLevel];
				if (success){
					[self goNextLevel];
				}else {
					[self showActivityIndicator];
				}
		}else if(location.y < 100.0f){
			[self goMenu];		
			busyUpgrading = NO;
			[self hideActivityIndicator];
		}
	}
	
}

-(void)dealloc{
	[super dealloc];
	[[NSNotificationCenter defaultCenter] removeObserver:self]; 
	[ai release];
}


@end
