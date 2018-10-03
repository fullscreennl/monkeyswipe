//
//  FinalTransition.m
//  MonkeySwipe
//
//  Created by johan ten broeke on 4/14/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "FinalTransition.h"
#import "OOOLevelManager.h"
#import "SimpleAudioEngine.h"

@implementation FinalTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	FinalTransition *layer = [FinalTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		bgImage = @"winall_cutscene_layer0.png";
		[self drawUI];
	}
	return self;
}

-(void)drawUI{
	
	CCSprite *bg = [CCSprite spriteWithFile:bgImage];
	bg.position =ccp(240.0f,160.0f);
	[self addChild:bg z:0 tag:2]; 
	
	CCSprite *king = [CCSprite spriteWithFile:@"winallcutscene_480_320_justking_colortweaked.png"];
	king.position =ccp(369.0f,237.0f);
	[self addChild:king z:0 tag:3]; 
	
	id move_action = [CCMoveBy actionWithDuration:0.5f position:ccp(0.0f,10.0f)];
	id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
	id easeBack_action = [ease_action reverse];
	id seq = [CCSequence actions:ease_action, easeBack_action, nil];
	[king runAction:[CCRepeatForever actionWithAction:seq]];
	
	
	CCSprite *overlay = [CCSprite spriteWithFile:@"winallcutscene_480_320_armleuning_colortweaked.png"];
	overlay.position =ccp(240.0f,160.0f);
	[self addChild:overlay z:0 tag:4]; 
	
	CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
	[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
	[self addChild:sheet z:0 tag:1];
	
	CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:[[OOOLevelManager sharedLevelManager] getTotalScore] fntFile:@"marker_felt2.fnt"];
	label1.position = ccp( 172, 181);
	//label1.scale = .5;
	[self addChild:label1];
	[[SimpleAudioEngine sharedEngine] playEffect:@"sfx_applause.mp3"];
	
	self.isTouchEnabled = YES;
	
}


- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	//UITouch *touch = [touches anyObject];
	//CGPoint location = [touch locationInView: [touch view]];
	[self goMenu];	
}

-(void)goMenu{
	id functioncall_action = [CCCallFunc actionWithTarget:self selector:@selector(loadMenu:)];
	id seq2 = [CCSequence actions:[CCDelayTime actionWithDuration: 0.0f],functioncall_action,nil]; 
	[self runAction:seq2];
}

-(void)loadMenu: (id)sel{
	//NSLog(@"goMenu");
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onReturnToMainMenu" 
					   object:nil 
					   userInfo:nil]];
}

-(void)dealloc{
	[super dealloc];
}


@end
