//
//  LevelPackMenu.m
//  MonkeySwipe
//
//  Created by Johan ten Broeke on 5/22/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "LevelPackMenu.h"
//#import "OpenFeint.h"
//#import "SampleOFDelegate.h"
#import "OOOLevelMap.h"
#import "HowToPlay.h"
#import "Settings.h"
#import "OOOLevelManager.h"
#import "Credits.h"
#import "SimpleAudioEngine.h"


@implementation LevelPackMenu

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	MainMenu *layer = [LevelPackMenu node];
	
	//BackgroundLayer *bgLayer = [BackgroundLayer layer];
	[scene addChild: layer];
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		map_ids = [[NSMutableArray array]retain];
		
		CGSize screenSize = [CCDirector sharedDirector].winSize;
		//CCLOG(@"Screen width in mainMenu %0.2f screen height %0.2f",screenSize.width,screenSize.height);
		CCSprite *sprite = [CCSprite spriteWithFile:@"splash_mockup.png"];
		[self addChild:sprite];
		sprite.position = ccp( screenSize.width/2, screenSize.height/2);
		CCSprite *titleSpr = [CCSprite spriteWithFile:@"monkey_swipe_title.png"];
		titleSpr.position=ccp(240.0f, 240.0f);
		[self addChild:titleSpr];
		
		
		CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
		[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
		[self addChild:sheet z:0 tag:1];
		
		CCMenu *menu = [CCMenu menuWithItems:nil];
		
		menu.position = ccp(240, 100);
		
		CCSprite *upsprite = nil;
		CCSprite *downsprite = nil;
		CCSprite *disabledsprite = nil;
		CCMenuItem *subItem = nil;
		NSString *text = nil;
		CCBitmapFontAtlas *textLabel = nil;
		
		NSMutableArray *textLabels = [NSMutableArray arrayWithCapacity:6];
		[textLabels addObject: @"BEGINNER"];
		[textLabels addObject: @"INTERMEDIATE"];
		[textLabels addObject: @"ADVANCED"];
		[textLabels addObject: @"CLASSIC!"];
		[textLabels addObject: @"<< MAIN MENU"];
		
		int x=0;
		for (x=0; x< 5; x++) {
			//if (x == 1 and [[OOOLevelManager sharedLevelManager] hasUpgraded] == NO){
			//	upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis.png"];
			//}else{
				upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn.png"];
			//}
			downsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_down.png"];
			disabledsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis.png"];
			//CCSprite *upsprite = [CCSprite spriteWithFile:@"generic_btn.png"];
			subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
											  selectedSprite:downsprite 
											  disabledSprite:disabledsprite 
													  target:self 
													selector:@selector(goPlay:)];	
			
			text = [textLabels objectAtIndex:x];
			
			NSNumber *m_id = [NSNumber numberWithInt:(x+1)];
			[map_ids addObject:m_id];
			subItem.userData = m_id;
			
			textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
			textLabel.position = ccp(round( subItem.contentSize.width / 2) ,round( subItem.contentSize.height / 2) - 8);
			
			textLabel.anchorPoint = ccp(0.5, 0.3);
			textLabel.scale = .5;
			[subItem addChild:textLabel z:99];	
			
			[menu addChild:subItem z:1 tag:1];
		}
		
		
		
		
		id move_action = [CCMoveBy actionWithDuration:1 position:ccp(0.0f,10.0f)];
		id ease_action = [CCEaseInOut actionWithAction:move_action rate:2];
		id easeBack_action = [ease_action reverse];
		id seq = [CCSequence actions:ease_action, easeBack_action, nil];
		[titleSpr runAction:[CCRepeatForever actionWithAction:seq]];
		
		CCSprite *decalSpr = [CCSprite spriteWithFile:@"decals.png"];
		decalSpr.position=ccp(240.0f, 160.0f);
		[self addChild:decalSpr];
		id fadeIn_action = [CCFadeIn actionWithDuration:3 ];
		[decalSpr runAction:[CCEaseIn actionWithAction:fadeIn_action rate:2]];
		
		
		
		//	[menu alignItemsVertically];
		
		int i=0;
		for( CCNode *child in [menu children] ) {
			if(i==4){
				child.position = ccp(0, 100 -  i*40);
			}else{
				child.position = ccp(0, 120 -  i*40);
			}
			CGPoint dstPoint = child.position;
			int offset = round(screenSize.width/2) + 150;
			if( i % 2 == 0)
				offset = -offset;
			
			id move = [CCMoveBy actionWithDuration:.6f position:ccp(dstPoint.x - offset,0)];
			//id action = [CCEaseElasticOut actionWithAction:move period:0.3f];
			id action = [CCEaseInOut actionWithAction:move rate:2.0f];
			child.position = ccp( dstPoint.x + offset, dstPoint.y);
			[child runAction:[CCSequence actions: [CCDelayTime actionWithDuration: .1f*i],action,nil ]];
			
			i++;
			
		}
		
		[self addChild:menu];
		
		ai = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleWhiteLarge];
		//[self resetObservers];
		
	}
	return self;
}	

-(void)onUpgrade:(NSNotification *)note{
	
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"onSurvivalModeEntered" 
					   object:nil 
					   userInfo:nil]];
}

-(void)onUpgradeFailed:(NSNotification *) note{
	//NSLog(@"upgrade failed %@ , %@",[note name],[note object]);
}

-(void)transactionFinished: (NSNotification *)note{
	[self hideActivityIndicator];
}

-(void) showActivityIndicator{
	busyUpgrading = YES;
	[ai setHidden:NO];
	[ai startAnimating];
	[ai setCenter:CGPointMake(320-75, 75)];
	[[[CCDirector sharedDirector] openGLView]  addSubview:ai];
}

-(void) hideActivityIndicator{
	busyUpgrading = NO;
	[ai removeFromSuperview];
}


-(void) goPlay: (id)sender{
	if(! busyUpgrading){
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		int button_id = [(NSNumber *)[sender userData] intValue];
		//[[SimpleAudioEngine sharedEngine] stopBackgroundMusic];
		if(button_id == 1){
			[[OOOLevelManager sharedLevelManager] switchContextLevelPack2];
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[OOOLevelMap scene]]];
		}else if (button_id == 2) {
			[[OOOLevelManager sharedLevelManager] switchContextLevelPack3];
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[OOOLevelMap scene]]];
		}else if (button_id == 3) {
			[[OOOLevelManager sharedLevelManager] switchContextLevelPack4];
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[OOOLevelMap scene]]];
		}else if (button_id == 4) {
			[[OOOLevelManager sharedLevelManager] switchContextLevelPack1];
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[OOOLevelMap scene]]];
		}else if (button_id == 5) {
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];
		}
	}
}


-(void) goSurvival: (id)sender
{
	//NSDictionary *userinfo = [NSDictionary dictionaryWithObjectsAndKeys:[sender userData],@"level_ind",nil];
	if ([[OOOLevelManager sharedLevelManager] hasUpgraded] == NO) {
		// subscribe to shop events //
		//[self resetObservers];
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onUpgrade:) 
													 name:@"upgradeSuccess" 
												   object:nil];
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onUpgradeFailed:) 
													 name:@"upgradeFailed" 
												   object:nil];
		
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(transactionFinished:) 
													 name:@"inAppPurchaseTransactionFailed" 
												   object:nil];
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(transactionFinished:) 
													 name:@"inAppPurchaseTransactionSuccess" 
												   object:nil];
		
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"onUpgradeRequested" 
						   object:nil 
						   userInfo:nil]];	
		[self showActivityIndicator];
	}else{
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"onSurvivalModeEntered" 
						   object:nil 
						   userInfo:nil]];
	}
}

- (void)dealloc {
	//NSLog(@"deallocing mainmenu");
	[map_ids release];
	[[NSNotificationCenter defaultCenter] removeObserver:self];
	[ai release];
    [super dealloc];
}




@end
