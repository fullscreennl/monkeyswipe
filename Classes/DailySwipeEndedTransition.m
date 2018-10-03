//
//  DailySwipeEndedTransition.m
//  MonkeySwipe
//
//  Created by Johan ten Broeke on 4/15/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "DailySwipeEndedTransition.h"
#import "OOOLevelManager.h"
#import "SimpleAudioEngine.h"


@implementation DailySwipeEndedTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	DailySwipeEndedTransition *layer = [DailySwipeEndedTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		bgImage = @"daily_swipe_cutscene_bg.png";
		[self drawUI];
	}
	return self;
}

-(void)drawUI{
	
	CCSprite *bg = [CCSprite spriteWithFile:bgImage];
	bg.position =ccp(240.0f,160.0f);
	[self addChild:bg z:0 tag:2]; 
	
	CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
	[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
	[self addChild:sheet z:0 tag:1];
	
	NSDictionary *daily_score = [[OOOLevelManager sharedLevelManager] getDailyScore];
	NSString *score = [[daily_score objectForKey:@"score"] stringValue];
	
	CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:score fntFile:@"MarkerFelt_Brown.fnt"];
	label1.position = ccp( 150, 75);
	//label1.scale = .5;
	[self addChild:label1];
	
	self.isTouchEnabled = YES;
	
}


- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	//UITouch *touch = [touches anyObject];
	//CGPoint location = [touch locationInView: [touch view]];
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
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
