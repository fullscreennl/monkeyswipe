//
//  LoseTransition.m
//  oneonone
//
//  Created by johan ten broeke on 3/17/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "LoseTransition.h"
#import "OOOLevelManager.h"

@implementation LoseTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	LoseTransition *layer = [LoseTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:@"Loading..." fntFile:@"marker_felt2.fnt"];
		label1.position = CGPointMake( 240, 210);
		[self addChild:label1];
		
		[self drawTitle:[[OOOLevelManager sharedLevelManager] getCurrentLevelTitle]];
		
		
	}
	return self;
}



-(void)drawTitle:(NSString*)_title
{
	CCBitmapFontAtlas *titleLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:_title fntFile:@"marker_felt2.fnt"];
	//NSLog(@"contentsize.width: %3.3f",titleLabel.contentSize.width);
	titleLabel.position = ccp(240.0,140);
	titleLabel.anchorPoint = ccp(0.5, 0.3);
	titleLabel.scale = 1;
	
	//id scale_action = [CCScaleBy actionWithDuration:1 scale:3.0f];
	//id ease_action = [CCEaseIn actionWithAction:scale_action rate:2];
	//id fadeOut_action = [CCFadeOut actionWithDuration:1 ];
	//id ease_alpha_action = [CCEaseIn actionWithAction:fadeOut_action rate:2];
	
	//[titleLabel runAction:ease_alpha_action];
	//[titleLabel runAction:ease_action];
	[self addChild:titleLabel];
}

- (void) onEnterTransitionDidFinish{
	
	id functioncall_action = [CCCallFunc actionWithTarget:self selector:@selector(reload:)];
	id seq2 = [CCSequence actions:[CCDelayTime actionWithDuration: 0.0f],functioncall_action,nil]; 
	[self runAction:seq2];

}

-(void)reload: (id)sel{
	//NSLog(@"reload !");
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"reloadLevel" 
					   object:nil 
					   userInfo:nil]];
}

@end
