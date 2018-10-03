//
//  OOOLevelMap.m
//  oneonone
//
//  Created by Johan ten Broeke on 3/2/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "OOOLevelMap.h"
#import "MainMenu.h"
#import "SimpleAudioEngine.h"
#import "Previews.h"
#import "LevelPackMenu.h"

@implementation OOOLevelMap

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	OOOLevelMap *layer = [OOOLevelMap node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

-(id) init
{
	if( (self=[super init])) {
		
		map_ids = [[NSMutableArray array]retain];
		//background image
		//CCSprite *bg = [CCSprite spriteWithFile:@"creditBG.png"];
		//bg.position =ccp(240.0f, 160.0f);
		//[self addChild:bg z:0 tag:1];
		pol =1;
		
		
		levelManager = [OOOLevelManager sharedLevelManager];
		[levelManager retain];
		
		CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
		[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
		[self addChild:sheet z:0 tag:1];
		CCSprite *sprite1 = [CCSprite spriteWithSpriteFrameName:@"level_map0001.png"];
		CCSprite *sprite2 = [CCSprite spriteWithSpriteFrameName:@"level_map0002.png"];
		CCSprite *sprite3 = [CCSprite spriteWithSpriteFrameName:@"level_map0003.png"];
		CCSprite *sprite4 = [CCSprite spriteWithSpriteFrameName:@"level_map0004.png"];
		CCSprite *sprite5 = [CCSprite spriteWithSpriteFrameName:@"level_map0005.png"];
		CCSprite *sprite6 = [CCSprite spriteWithSpriteFrameName:@"level_map0006.png"];
		
		//sprite.position = CGPointMake(100, 100);
		//[sheet addChild:sprite z:0 tag:2];
		CCMenu *menu1 = [CCMenu menuWithItems:nil];
		CCMenu *menu2 = [CCMenu menuWithItems:nil];
		CCMenu *menu3 = [CCMenu menuWithItems:nil];
		CCMenu *menu4 = [CCMenu menuWithItems:nil];
		CCMenu *menu5 = [CCMenu menuWithItems:nil];
		CCMenu *menu6 = [CCMenu menuWithItems:nil];
		CCMenu *menu7 = [CCMenu menuWithItems:nil];
		CCMenu *menu8 = [CCMenu menuWithItems:nil];
		CCMenu *menu9 = [CCMenu menuWithItems:nil];
		
		int currentLevel = [levelManager getLevelProgressionIndex];
		NSArray * levels = [levelManager getLevels];
		int arrayCount = [levels count];
		for (int i = 0; i < arrayCount; i++) {

			int score = [[[levels objectAtIndex:i] objectForKey:@"score"] intValue];
			int num_stars = [levelManager getStarsForScore:score];
				
			CCSprite* upsprite;
			
			if (num_stars == 3) {
				upsprite = sprite1;
			}else if (num_stars == 2) {
				upsprite = sprite2;
			}else{
				upsprite = sprite3;
			}
			
			if (i == currentLevel){
				upsprite = sprite6;
			}
			
			CCMenuItemSprite *map_item = [CCMenuItemSprite itemFromNormalSprite:upsprite 
											   selectedSprite:sprite5 
											   disabledSprite:sprite4 
													   target:self 
													 selector:@selector(menuCallback:)];	
			
			NSNumber *m_id = [NSNumber numberWithInt:i];
			[map_ids addObject:m_id];
			map_item.userData = m_id;
			
			NSString *text = [NSString stringWithString: [[NSNumber numberWithInt:(i+1)] stringValue]];
			CCBitmapFontAtlas *textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"marker_felt2.fnt"];
			textLabel.position = ccp(round( map_item.contentSize.width / 2)+24 ,round( map_item.contentSize.height / 2) - 16);
			
			textLabel.anchorPoint = ccp(0.5, 0.3);
			textLabel.scale = .9;
			[map_item addChild:textLabel z:99];	
			
			
			
			map_item.scale= .9;
			if (i > currentLevel){
				map_item.isEnabled = NO;
			}
			if (i < 5){
				[menu1 addChild:map_item z:0 tag:i];
			}else if (i < 10){
				[menu2 addChild:map_item z:0 tag:i];
			}else if (i < 15){
				[menu3 addChild:map_item z:0 tag:i];
			}else if (i < 20){
				[menu4 addChild:map_item z:0 tag:i];
			}else if (i < 25){
				[menu5 addChild:map_item z:0 tag:i];
			}else if (i < 30){
				[menu6 addChild:map_item z:0 tag:i];
			}else if (i < 35){
				[menu7 addChild:map_item z:0 tag:i];
			}else if (i < 40){
				[menu8 addChild:map_item z:0 tag:i];
			}else if (i < 45){
				[menu9 addChild:map_item z:0 tag:i];
			}
		}
		
		//[menu alignItemsHorizontallyWithPadding:5.0];
		//[menu2 alignItemsHorizontallyWithPadding:0.0];
		
		//[menu alignItemsInColumns:[NSNumber numberWithInt:5],[NSNumber numberWithInt:5],[NSNumber numberWithInt:5],[NSNumber numberWithInt:5],nil];
		//[menu2 alignItemsInColumns:[NSNumber numberWithInt:5],[NSNumber numberWithInt:5],[NSNumber numberWithInt:5],[NSNumber numberWithInt:5],nil];
		
		
		
		[menu1 alignItemsHorizontallyWithPadding:5.0];
		[menu2 alignItemsHorizontallyWithPadding:5.0];
		[menu3 alignItemsHorizontallyWithPadding:5.0];
		[menu4 alignItemsHorizontallyWithPadding:5.0];
		[menu5 alignItemsHorizontallyWithPadding:5.0];
		[menu6 alignItemsHorizontallyWithPadding:5.0];
		[menu7 alignItemsHorizontallyWithPadding:5.0];
		[menu8 alignItemsHorizontallyWithPadding:5.0];
		
		//menu.scaleX = 0.85;
		//menu.scaleY = 0.85;
		
		//menu2.scaleX = 0.85;
		//menu2.scaleY = 0.85;
		menucont1 = [CCLayer node];
		menucont2 = [CCLayer node];
		int yspacing = 58 + 5;
		int toppos = 280;
		menu1.position = ccp(240.0, toppos);
		menu2.position = ccp(240.0, toppos - yspacing);
		menu3.position = ccp(240.0, toppos- 2*yspacing);		
		menu4.position = ccp(240.0, toppos- 3*yspacing);
		menu5.position = ccp(240.0, toppos);
		menu6.position = ccp(240.0, toppos- yspacing);
		menu7.position = ccp(240.0, toppos - 2*yspacing);
		menu8.position = ccp(240.0, toppos- 3*yspacing);		

		[menucont1 addChild:menu1];
		[menucont1 addChild:menu2];
		[menucont1 addChild:menu3];
		[menucont1 addChild:menu4];
		[menucont2 addChild:menu5];
		[menucont2 addChild:menu6];
		[menucont2 addChild:menu7];
		[menucont2 addChild:menu8];
		[self addChild:menucont1];
		[self addChild:menucont2];
		menucont2.position =ccp(1.5 *480 , 0);
	}
	
	//CCBitmapFontAtlas *label1 = [CCBitmapFontAtlas bitmapFontAtlasWithString:@"Monkey Swipe to the resque!" fntFile:@"markerfelt.fnt"];
	//label1.position = CGPointMake( 240, 30);
	//[self addChild:label1];
	[self buildSubMenu];
	if ([levelManager getLevelProgressionIndex] > 19) {
		[self goNextLevels];
	}
	return self;
	
}


-(void) buildSubMenu
{
	//CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
	//[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
	//[self addChild:sheet z:0 tag:1];
	//CCSpriteSheet *sheet = (CCSpriteSheet*)[self getChildByTag:1];
	CCSprite *upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn.png"];
	CCSprite *downsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_down.png"];
	CCSprite *disabledsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis.png"];
	//CCSprite *upsprite = [CCSprite spriteWithFile:@"generic_btn.png"];
	
	subMenu = [CCMenu menuWithItems:nil];
	NSMutableArray *textLabels = [NSMutableArray arrayWithCapacity:3];
	[textLabels addObject: @"MENU"];
	[textLabels addObject: @"PREVIEW"];
	[textLabels addObject: @">>> 21/40      "];
	int x=0;
	for(x=0;x<3;x++){
		CCMenuItem *subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
												  selectedSprite:downsprite 
												  disabledSprite:disabledsprite 
														  target:self 
														selector:@selector(subMenuCallback:)];	
		
		NSNumber *m_id = [NSNumber numberWithInt:(x+1)];
		[map_ids addObject:m_id];
		subItem.userData = m_id;
		
		NSString *text = [textLabels objectAtIndex:x];
		
		CCBitmapFontAtlas *textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2) ,round( subItem.contentSize.height / 2) - 8);
	
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
	
		
		[subMenu addChild:subItem z:1 tag:1];
	}
	
	subMenu.position = ccp(240, 30);
	[subMenu alignItemsHorizontallyWithPadding:0];
	[self addChild:subMenu];
	
	
	subMenu2 = [CCMenu menuWithItems:nil];
	NSMutableArray *textLabels2 = [NSMutableArray arrayWithCapacity:3];
	[textLabels2 addObject: @"MENU"];
	[textLabels2 addObject: @"PREVIEW"];
	[textLabels2 addObject: @"<<< 1/20     "];
	//int x=0;
	for(x=0;x<3;x++){
		CCMenuItem *subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
													  selectedSprite:downsprite 
													  disabledSprite:disabledsprite 
															  target:self 
															selector:@selector(subMenuCallback:)];	
		
		NSNumber *m_id = [NSNumber numberWithInt:(x+1)];
		[map_ids addObject:m_id];
		subItem.userData = m_id;
		
		NSString *text = [textLabels2 objectAtIndex:x];
		
		CCBitmapFontAtlas *textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2) ,round( subItem.contentSize.height / 2) - 8);
		
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
		
		
		[subMenu2 addChild:subItem z:1 tag:1];
	}
	subMenu2.position = ccp(240, -30);
	[subMenu2 alignItemsHorizontallyWithPadding:0];
	[self addChild:subMenu2];
	
}


-(void) menuCallback: (id) sender
{
	//NSLog(@"menu cliked -> !%@",sender);
	//NSLog(@"menu cliked -> !%@",[sender userData]);
	NSDictionary *userinfo = [NSDictionary dictionaryWithObjectsAndKeys:[sender userData],@"level_ind",
																		[NSNumber numberWithBool:[levelManager hasTutorial]],@"tutorial",
																		nil];
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"levelEntered" 
					   object:nil 
					   userInfo:userinfo]];
	
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
}

-(void) subMenuCallback: (id) sender
{
	if([(NSNumber *)[sender userData] intValue] == 1){
		[self goSettings];
	}else if([(NSNumber *)[sender userData] intValue] == 2){
		[self goPreview];
	}else if([(NSNumber *)[sender userData]intValue] == 3){
		[self goNextLevels];
	}
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	
}


-(void) goNextLevels
{
	
	
	pol = -1*pol;
	if(pol==-1){
		subMenu2.position = ccp(240, -30);
		subMenu.position = ccp(240, 30);
		menucont2.position =ccp(1.5 *480 , 0);
		menucont1.position = ccp(0,0);
	}else{
		subMenu2.position = ccp(240, 30);
		subMenu.position = ccp(240, -30);
		menucont2.position =ccp(0 , 0);
		menucont1.position = ccp(-1.5 *480,0);
	}
	//menucont2.position =ccp(0 , 0);
	id move = [CCMoveBy actionWithDuration:2.0f position:ccp(pol*1.5*480,0)];
	id moveEased = [CCEaseElasticOut actionWithAction:move period:.3]; 
	[menucont2 runAction:moveEased]; 
	id move2 = [CCMoveBy actionWithDuration:2.0f position:ccp(pol*1.5*480,0)];
	id moveEased2 = [CCEaseElasticOut actionWithAction:move2 period:.3];
	[menucont1 runAction:moveEased2];
	
	id move3 = [CCMoveBy actionWithDuration:2.0f position:ccp(0,pol*60)];
	id moveEased3 = [CCEaseElasticOut actionWithAction:move3 period:.3]; 
	[subMenu runAction:moveEased3]; 
	id move4 = [CCMoveBy actionWithDuration:2.0f position:ccp(0,-1*pol*60)];
	id moveEased4 = [CCEaseElasticOut actionWithAction:move4 period:.3];
	[subMenu2 runAction:moveEased4];
	
	//menucont1.position =ccp(1.5 *480 , 0);
}


-(void) goPreview
{
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[Previews scene]]];
}
		
-(void) goSettings		
{
	//NSLog(@"going settings");
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[LevelPackMenu scene]]];
}

-(void)dealloc{
	[levelManager release];
	[map_ids release];
	[super dealloc];
}
		
@end
