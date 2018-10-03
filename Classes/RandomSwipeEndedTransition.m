//
//  DailySwipeEndedTransition.m
//  MonkeySwipe
//
//  Created by Johan ten Broeke on 4/15/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "RandomSwipeEndedTransition.h"
#import "OOOLevelManager.h"
#import "SimpleAudioEngine.h"


@implementation RandomSwipeEndedTransition

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	RandomSwipeEndedTransition *layer = [RandomSwipeEndedTransition node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		bgImage = @"randomwinscene.png";
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
	
	NSDictionary *daily_score = [[OOOLevelManager sharedLevelManager] getRandomScore];
	NSString *score = [[daily_score objectForKey:@"score"] stringValue];
	
	CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:score fntFile:@"MarkerFelt_Brown.fnt"];
	label1.position = ccp( 145, 160);
	label1.rotation = 4;
	//label1.scale = .5;
	[self addChild:label1];
	
	CCSprite *monkeyHand = [CCSprite spriteWithSpriteFrameName:@"monkeyhand.png"];
	monkeyHand.position=ccp(80.0f, 40.0f);
	monkeyHand.scale = .7;
	[sheet addChild:monkeyHand];
	
	id move_action = [CCMoveBy actionWithDuration:1 position:ccp(0.0f,10.0f)];
	id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
	id easeBack_action = [ease_action reverse];
	id seq = [CCSequence actions:ease_action, easeBack_action, nil];
	[monkeyHand runAction:[CCRepeatForever actionWithAction:seq]];
	
	
	
	
	CCSprite *starInd;
	NSNumber *numStars = [daily_score objectForKey:@"stars"]; 
	//NSLog(@"numStars: %i",[numStars intValue]);
	if([numStars intValue]==1){
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0003.png"];
	}else if([numStars intValue]==2){
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0002.png"];
	}else{
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0001.png"];
	}
	
	//NSLog(@"num stars --> %@",[[OOOLevelManager sharedLevelManager] getNumStarsForPrevLevel]);
	
	
	
	[sheet addChild:starInd];
	starInd.position = ccp(366.0, 181.0);
	starInd.rotation = -4;
	
	NSNumber *secondsPassed = [daily_score objectForKey:@"seconds"];
	NSString *secondsLine = [[secondsPassed stringValue] stringByAppendingString:@" s"];
	CCLabel *secondsLabel = [CCLabel labelWithString:secondsLine fontName:@"Marker Felt" fontSize:20.0];
	[secondsLabel setColor:ccc3(91,68,0)];
	secondsLabel.position =ccp(295.0,158.0);
	[self addChild:secondsLabel];

	NSString *swipesUsed = [[daily_score objectForKey:@"swipes"] stringValue];
	
	CCLabel *swipeLabel = [CCLabel labelWithString:swipesUsed fontName:@"Marker Felt" fontSize:20.0];
	[swipeLabel setColor:ccc3(91,68,0)];
	swipeLabel.position =ccp(295.0,180.0);
	[self addChild:swipeLabel];
	
	CCMenu *menu = [CCMenu menuWithItems:nil];
	menu.position = ccp(240, 100);
	CCSprite *randomSwipe =[CCSprite spriteWithSpriteFrameName:@"randomSwipe.png"];
	CCSprite *randomSwipeDown =[CCSprite spriteWithSpriteFrameName:@"randomSwipeDown.png"];
	CCMenuItem *subItem = nil;
	subItem = [CCMenuItemSprite itemFromNormalSprite:randomSwipe 
									  selectedSprite:randomSwipeDown 
									  disabledSprite:randomSwipe 
											  target:self 
											selector:@selector(goRandomSwipe:)];
	[menu addChild:subItem];
	subItem.position = ccp(200, 170);
	subItem.scale=.6;
	[self addChild:menu];
	self.isTouchEnabled = YES;
	
}

-(void) goRandomSwipe:(id)sender{
	[[NSNotificationCenter defaultCenter] postNotification:[NSNotification 
															notificationWithName:@"onRandomLevel" 
															object:nil 
															userInfo:nil]];
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
