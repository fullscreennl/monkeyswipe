//
//  WinTransition.m
//  oneonone
//
//  Created by johan ten broeke on 3/22/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "WinTransition.h"
#import "OOOLevelManager.h"
#import "SimpleAudioEngine.h"
#import <UIKit/UIKit.h>


@implementation WinTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	WinTransition *layer = [WinTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {	
		if ([self isMemberOfClass:[WinTransition class]]){
			bgImage = @"win_cutscene_bg.png";
			[self drawUI];
		}
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
	
	CCSprite *monkeyHand = [CCSprite spriteWithSpriteFrameName:@"monkeyhand.png"];
	monkeyHand.position=ccp(60.0f, 50.0f);
	[sheet addChild:monkeyHand];
	
	id move_action = [CCMoveBy actionWithDuration:1 position:ccp(0.0f,10.0f)];
	id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
	id easeBack_action = [ease_action reverse];
	id seq = [CCSequence actions:ease_action, easeBack_action, nil];
	[monkeyHand runAction:[CCRepeatForever actionWithAction:seq]];
	
	
	
	
	CCSprite *starInd;
	NSNumber *numStars = [[OOOLevelManager sharedLevelManager] getNumStarsForPrevLevel]; 
	//NSLog(@"numStars: %i",[numStars intValue]);
	if([numStars intValue]==1){
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0003.png"];
	}else if([numStars intValue]==2){
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0002.png"];
	}else{
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0001.png"];
	}
	
	//NSLog(@"num stars --> %@",[[OOOLevelManager sharedLevelManager] getNumStarsForPrevLevel]);
	
	CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:[[OOOLevelManager sharedLevelManager] getResultsForPrevLevel] fntFile:@"marker_felt2.fnt"];
	label1.position = ccp( 385, 214);
	//label1.scale = .5;
	[self addChild:label1];
	
	[sheet addChild:starInd];
	starInd.position = ccp(385.0, 181.0);
	//starInd.scale=.45;
	
	
	if ([[OOOLevelManager sharedLevelManager] scoreIsHighScore]==YES ) {
		CCSprite *highScoreDecal = [CCSprite spriteWithSpriteFrameName:@"highscore_decal.png"];
		[self addChild:highScoreDecal z:1 tag:1];
		highScoreDecal.position =ccp(377, 248);
	}
	
	NSNumber *secondsPassed = [[OOOLevelManager sharedLevelManager] getTimeForPrevLevel];
	NSString *secondsLine = [[secondsPassed stringValue] stringByAppendingString:@" s"];
	CCLabel *secondsLabel = [CCLabel labelWithString:secondsLine fontName:@"Marker Felt" fontSize:20.0];
	[secondsLabel setColor:ccc3(0,0,0)];
	secondsLabel.position =ccp(295.0,158.0);
	[self addChild:secondsLabel];
	
	NSString *levelNumber = [NSString stringWithFormat:@"level %i",([[OOOLevelManager sharedLevelManager] getCurrentLevelIndex])+1];
	CCLabel *levelLabel = [CCLabel labelWithString:levelNumber fontName:@"Marker Felt" fontSize:20.0];
	[levelLabel setColor:ccc3(50,50,50)];
	levelLabel.position =ccp(295.0,248.0);
	[self addChild:levelLabel];
	
	
	NSNumber *swipesUsed = [[OOOLevelManager sharedLevelManager] getNumSwipesForPrevLevel];
	
	CCLabel *swipeLabel = [CCLabel labelWithString:[swipesUsed stringValue] fontName:@"Marker Felt" fontSize:20.0];
	[swipeLabel setColor:ccc3(0,0,0)];
	swipeLabel.position =ccp(295.0,180.0);
	[self addChild:swipeLabel];
	
	
	self.isTouchEnabled = YES;

}

- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	UITouch *touch = [touches anyObject];
	CGPoint location = [touch locationInView: [touch view]];
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	//NSLog(@"touches pos: %3f",location.y);
	if(location.x > 352.0f ) {
		[[OOOLevelManager sharedLevelManager] incrementLevel];
		[self goNextLevel];
	}else if(location.x < 100.0f){
		[self goMenu];
	}else{
		[self goNextLevel];
	}
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
					   notificationWithName:@"goBack" 
					   object:nil 
					   userInfo:nil]];
}

- (void) goNextLevel{	
	id functioncall_action = [CCCallFunc actionWithTarget:self selector:@selector(reload:)];
	id seq2 = [CCSequence actions:[CCDelayTime actionWithDuration: 0.0f],functioncall_action,nil]; 
	[self runAction:seq2];
}

-(void)reload: (id)sel{
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"reloadLevel" 
					   object:nil 
					   userInfo:nil]];
}

-(void)dealloc{
	[super dealloc];
}

@end
