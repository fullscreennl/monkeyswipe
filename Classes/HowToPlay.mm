//
//  MainSplash.mm
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//



#import "HowToPlay.h"
//#import "button.h"
#import "MainMenu.h"
#import "SimpleAudioEngine.h"



@implementation HowToPlay

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	HowToPlay *layer = [HowToPlay node];
	
	//BackgroundLayer *bgLayer = [BackgroundLayer layer];
	[scene addChild: layer];
	// return the scene
	return scene;
}


-(id) init
{
	if( (self=[super init])) {
		CGSize screenSize = [CCDirector sharedDirector].winSize;
		//CCLOG(@"Screen width in mainMenu %0.2f screen height %0.2f",screenSize.width,screenSize.height);
		//CCSprite *sprite = [CCSprite spriteWithFile:@"howtoplay.png"];
		CCSprite *sprite = [CCSprite spriteWithFile:@"creditBG_3_refl.png"];
		[self addChild:sprite];
		sprite.position = ccp( screenSize.width/2, screenSize.height/2);
		CCMenu *menu = [CCMenu menuWithItems:nil];
		//menu.position = ccp(240, 160);
		
		CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
		[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
		[self addChild:sheet z:0 tag:674];
		
		CCSprite *upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn.png"];
		CCSprite *downsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_down.png"];
		CCSprite *disabledsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis.png"];
		//CCSprite *upsprite = [CCSprite spriteWithFile:@"generic_btn.png"];
		CCMenuItem *subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
													  selectedSprite:downsprite 
													  disabledSprite:disabledsprite 
															  target:self 
															selector:@selector(goBack:)];	
		
		NSString *text = @"MENU";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		CCBitmapFontAtlas *textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2)-20 ,round( subItem.contentSize.height / 2) - 8);
		
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
		
		[menu addChild:subItem z:1 tag:1];
		subItem.position = ccp(100, 120);
		CGPoint dstPoint = subItem.position;
		int offset = round(screenSize.width/2) + 150;
		id movebtn = [CCMoveBy actionWithDuration:2 position:ccp(dstPoint.x - offset,0)];
		id actionbtn = [CCEaseElasticOut actionWithAction:movebtn period:0.3f];
		
		subItem.position = ccp( dstPoint.x + offset, dstPoint.y);
		[subItem runAction:actionbtn];
		
	
		
		CCSprite *ani = [CCSprite spriteWithFile:@"tutorial/monkeyswipe_tutorial 01.png"];
		
		anim = [[CCAnimation animationWithName:@"how_to" delay:0.3f] retain];
		for (int i=1; i<23; i++){
			//NSLog(@"spritename: %@",[NSString stringWithFormat:@"howto%01d.png",i]);
			if(i<10){
				[anim addFrameWithFilename:[NSString stringWithFormat:@"tutorial/monkeyswipe_tutorial 0%1d.png",i]];
			}else{
				[anim addFrameWithFilename:[NSString stringWithFormat:@"tutorial/monkeyswipe_tutorial %1d.png",i]];
			}
		}
									
		[ani runAction:[CCRepeatForever actionWithAction: [CCAnimate actionWithAnimation:anim restoreOriginalFrame:YES]]];
		[self addChild:ani];
		ani.position =ccp(240, 180);
		ani.rotation = -5;
		
		NSString *howToText = @"Swipe anywhere on screen to make the Monkey move!";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		CCBitmapFontAtlas *howToTextLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:howToText fntFile:@"MarkerFelt_Brown.fnt"];
		howToTextLabel.position = ccp(240 ,40);
		howToTextLabel.scale = .4;
		[self addChild:howToTextLabel];	
		
		NSString *howToText2 = @"Change the monkey's direction at any time by continuous swiping..";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		CCBitmapFontAtlas *howToTextLabel2 = [CCBitmapFontAtlas bitmapFontAtlasWithString:howToText2 fntFile:@"MarkerFelt_Brown.fnt"];
		howToTextLabel2.position = ccp(240 ,15);
		howToTextLabel2.scale = .3;
		[self addChild:howToTextLabel2];	
		
		[self addChild:menu];
		
				
		
	}
	return self;
}	




-(void) goBack: (id)sender
{
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];
}



- (void)dealloc {
	//NSLog(@"deallocing howtoplay");
	[anim release];
    [super dealloc];
}


@end
