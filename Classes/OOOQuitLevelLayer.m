//
//  OOOQuitLevelLayer.m
//  oneonone
//
//  Created by johan ten broeke on 3/24/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "OOOQuitLevelLayer.h"


@implementation OOOQuitLevelLayer

+(id) layer
{
	OOOQuitLevelLayer *layer = [OOOQuitLevelLayer node];
	return layer;
}

-(id) init
{
	if( (self=[super init])) {
		
		self.isTouchEnabled = YES;
		
		CCMenu *menu = [CCMenu menuWithItems:nil];
		
		CCSprite *sprite1 = [CCSprite spriteWithSpriteFrameName:@"back_button0001.png"];
		CCSprite *sprite2 = [CCSprite spriteWithSpriteFrameName:@"back_button0002.png"];
		CCSprite *sprite3 = [CCSprite spriteWithSpriteFrameName:@"back_button0003.png"];
		
		CCMenuItemSprite *item = [CCMenuItemSprite itemFromNormalSprite:sprite1 
									   selectedSprite:sprite2 
									   disabledSprite:sprite3 
											   target:self 
											 selector:@selector(goMenu:)];	
		[menu addChild:item];
		menu.position = ccp(20,320 - 20);
		[self addChild:menu];
	}
	return self;
}


-(void) goMenu: (id) sender
{
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onLeaveLevel" 
					   object:nil
					   userInfo:nil]];
}

@end
