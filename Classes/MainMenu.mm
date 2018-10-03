//
//  MainSplash.mm
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//


//#import "OpenFeint.h"
//#import "SampleOFDelegate.h"
#import "MainMenu.h"
//#import "button.h"
#import "OOOLevelMap.h"
#import "HowToPlay.h"
#import "Settings.h"
#import "OOOLevelManager.h"
#import "Credits.h"
#import "SimpleAudioEngine.h"
#import "LevelPackMenu.h"




@implementation MainMenu

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	MainMenu *layer = [MainMenu node];
	
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
		[textLabels addObject: @"PLAY THE GAME"];
		[textLabels addObject: @"SURVIVAL"];
		[textLabels addObject: @"HIGH SCORES"];
		[textLabels addObject: @"HOW TO PLAY?"];
		[textLabels addObject: @"SETTINGS"];
		[textLabels addObject: @"CREDITS"];
				
		int x=0;
		for (x=0; x< 6; x++) {
			if (x == 1 and [[OOOLevelManager sharedLevelManager] hasUpgraded] == NO){
				upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis.png"];
			}else{
				upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn.png"];
			}
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
		
		
		//	[menu alignItemsVertically];
		
		int i=0;
		for( CCNode *child in [menu children] ) {
			child.position = ccp(0, 120 -  i*40);
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
		
		/*
		
		//dailySwipe item
		
		CCSprite *dailySwipe =[CCSprite spriteWithSpriteFrameName:@"dailySwipe.png"];
		CCSprite *dailySwipeDown =[CCSprite spriteWithSpriteFrameName:@"dailySwipeDown.png"];
		subItem = [CCMenuItemSprite itemFromNormalSprite:dailySwipe 
										  selectedSprite:dailySwipeDown 
										  disabledSprite:dailySwipe 
												  target:self 
												selector:@selector(goDailySwipe:)];
		[menu addChild:subItem];
		subItem.position = ccp(-168, -38);
		//end dailySwipe
		*/
		
		//dailySwipe item
		
		CCSprite *randomSwipe =[CCSprite spriteWithSpriteFrameName:@"randomSwipe.png"];
		CCSprite *randomSwipeDown =[CCSprite spriteWithSpriteFrameName:@"randomSwipeDown.png"];
		subItem = [CCMenuItemSprite itemFromNormalSprite:randomSwipe 
										  selectedSprite:randomSwipeDown 
										  disabledSprite:randomSwipe 
												  target:self 
												selector:@selector(goRandomSwipe:)];
		[menu addChild:subItem];
		subItem.position = ccp(-168, -38);
		
		if([[OOOLevelManager sharedLevelManager] hasUpgraded] == NO){
			CCSprite *randomLock = [CCSprite spriteWithSpriteFrameName:@"lockonRanSwipe.png"];
			[subItem addChild:randomLock];
			randomLock.position = ccp(97,105);
		}
		
		
		//end dailySwipe
		
		
		
		
		
		[self addChild:menu];
		
		ai = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleWhiteLarge];
		[self resetObservers];
		
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

-(void)onUpgrade2:(NSNotification *)note{
	[[NSNotificationCenter defaultCenter]	
		postNotification:[NSNotification 
		notificationWithName:@"onRandomLevel" 
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

-(void) goScores:(id)sender
{
	//TODO gamecenter scoreboard
	//[OpenFeint launchDashboardWithListLeaderboardsPage];
    [[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName:@"showLeaderboard" object:nil]];
}




-(void) goPlay: (id)sender{
	if(! busyUpgrading){
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		int button_id = [(NSNumber *)[sender userData] intValue];
		
		//[[SimpleAudioEngine sharedEngine] stopBackgroundMusic];
		if(button_id == 1){
			//[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[OOOLevelMap scene]]];
			[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[LevelPackMenu scene]]];
		}else if (button_id == 2) {
			[self goSurvival:nil];
		}else if (button_id == 3) {
			[self goScores:nil];
		}else if (button_id == 4) {
			[self goTutorial:nil];
		}else if (button_id == 5) {
			[self goSettings:nil];
		}else if (button_id == 6) {
			[self goCredits:nil];
		}
	}
}


-(void)resetObservers{
	[[NSNotificationCenter defaultCenter] removeObserver:self];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(loadingDailySwipe:) 
												 name:@"loadingDailySwipe" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(loadingDailySwipeDone:) 
												 name:@"loadingDailySwipeDone" 
											   object:nil];
}

-(void)loadingDailySwipe:(NSNotification *)note{
	//NSLog(@"startloding swipe!");
	[self showActivityIndicator];
}

-(void)loadingDailySwipeDone:(NSNotification *)note{
	//NSLog(@"done loading swipe!");
	[self hideActivityIndicator];
}

-(void) goDailySwipe:(id)sender{
	if(! busyUpgrading){
		//NSLog(@"goDailySwipe pushed");
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"onDailyLevel" 
						   object:nil 
						   userInfo:nil]];
	}
}

-(void)showAlert:(NSString *)msg{
	UIAlertView *myAlert = [[UIAlertView alloc] initWithTitle:@"Want to upgrade?"
													  message:msg
													 delegate:self
											cancelButtonTitle:@"No"
											otherButtonTitles:@"Yes!",nil];
	[myAlert show];
}

- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex{
	

	if(buttonIndex == 0){
		[self resetObservers];
	}else{
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
	}

	[alertView release];
}

-(void) goRandomSwipe:(id)sender{
	if(! busyUpgrading){
		//NSLog(@"goDailySwipe pushed");
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		if ([[OOOLevelManager sharedLevelManager] hasUpgraded] == NO) {
			
			// subscribe to shop events //
			[self resetObservers];
			
			[[NSNotificationCenter defaultCenter] addObserver:self 
													 selector:@selector(onUpgrade2:) 
														 name:@"upgradeSuccess" 
													   object:nil];
			
			[self showAlert:@"Do you want to unlock Random play, and Survival mode and get access to all 160 levels for just $0.99 (or equiv.)?"];
		}else{
			[[NSNotificationCenter defaultCenter]	postNotification:[NSNotification 
												notificationWithName:@"onRandomLevel" 
															object:nil 
															userInfo:nil]];
		}		
	}
}



-(void) goSurvival: (id)sender
{
	//NSDictionary *userinfo = [NSDictionary dictionaryWithObjectsAndKeys:[sender userData],@"level_ind",nil];
	if ([[OOOLevelManager sharedLevelManager] hasUpgraded] == NO) {
		// subscribe to shop events //
		[self resetObservers];
		
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onUpgrade:) 
													 name:@"upgradeSuccess" 
												   object:nil];
		
		[self showAlert:@"Do you want to unlock Survival play, and Random mode and get access to all 160 levels for just $0.99 (or equiv.)?"];
	
	}else{
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"onSurvivalModeEntered" 
						   object:nil 
						   userInfo:nil]];
	}
}


-(void) goCredits: (id)sender
{
	[[SimpleAudioEngine sharedEngine] playEffect:@"paybacktime.wav"];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[Credits scene]]];	
}


-(void) goTutorial: (id)sender
{
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[HowToPlay scene]]];
}


-(void) goSettings: (id)sender
{
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[Settings scene]]];
}

- (void)dealloc {
	//NSLog(@"deallocing mainmenu");
	[map_ids release];
	[[NSNotificationCenter defaultCenter] removeObserver:self];
	[ai release];
    [super dealloc];
}


@end
