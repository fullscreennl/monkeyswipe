//
//  MainSplash.mm
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/25/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//



#import "Previews.h"
//#import "button.h"
#import "MainMenu.h"
#import "SimpleAudioEngine.h"
#import "OOOLevelManager.h"


@implementation Previews

+(id) scene
{
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];
	
	// 'layer' is an autorelease object.
	Previews *layer = [Previews node];
	
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
		CCSprite *sprite = [CCSprite spriteWithFile:@"creditBG_3.png"];
		[self addChild:sprite];
		sprite.position = ccp( screenSize.width/2, screenSize.height/2);
		
		
		
		CCSprite *imageBG = [CCSprite spriteWithFile:@"previewimageBG.png"];
		[self addChild: imageBG];
		imageBG.position = ccp(140, 160);
		
		
		
		CCMenu *menu = [CCMenu menuWithItems:nil];
		//menu.position = ccp(240, 160);
		
		previewIndex=0;
		
		
		CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
		[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
		[self addChild:sheet z:0 tag:674];
		
		CCSprite *upsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn.png"];
		CCSprite *downsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_down.png"];
		CCSprite *disabledsprite =[CCSprite spriteWithSpriteFrameName:@"generic_btn_dis_nodecal.png"];
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

		
		//play btn
		subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
													  selectedSprite:downsprite 
													  disabledSprite:disabledsprite 
															  target:self 
															selector:@selector(goLevel:)];	
		
		text = @"PLAY NOW";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2)-20 ,round( subItem.contentSize.height / 2) - 8);
		
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
		
		[menu addChild:subItem z:1 tag:1];
		subItem.position = ccp(100, 66);
		dstPoint = subItem.position;
		offset = round(screenSize.width/2) + 150;
		id movebtn4 = [CCMoveBy actionWithDuration:2 position:ccp(dstPoint.x - offset,0)];
		id actionbtn4 = [CCEaseElasticOut actionWithAction:movebtn4 period:0.3f];
		
		subItem.position = ccp( dstPoint.x + offset, dstPoint.y);
		[subItem runAction:actionbtn4];
		playBTN = subItem;
		//end play btn
		
		
		
		
		subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
													  selectedSprite:downsprite 
													  disabledSprite:disabledsprite 
															  target:self 
															selector:@selector(goNext:)];	
		
		text = @"NEXT";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2)-20 ,round( subItem.contentSize.height / 2) - 8);
		
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
		
		[menu addChild:subItem z:1 tag:1];
		nextBTN = subItem;
		subItem.position = ccp(100, -120);
		dstPoint = subItem.position;
		offset = round(screenSize.width/2) + 150;
		id movebtn2 = [CCMoveBy actionWithDuration:2 position:ccp(dstPoint.x - offset,0)];
		id actionbtn2 = [CCEaseElasticOut actionWithAction:movebtn2 period:0.3f];
		
		subItem.position = ccp( dstPoint.x + offset, dstPoint.y);
		[subItem runAction:actionbtn2];
		
		subItem = [CCMenuItemSprite itemFromNormalSprite:upsprite 
										  selectedSprite:downsprite 
										  disabledSprite:disabledsprite 
												  target:self 
												selector:@selector(goPrev:)];	
		
		text = @"          PREV";
		//subItem.userData = [[NSNumber numberWithInt:1] retain];
		textLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:text fntFile:@"MarkerFelt_Brown.fnt"];
		textLabel.position = ccp(round( subItem.contentSize.width / 2)-20 ,round( subItem.contentSize.height / 2) - 8);
		
		textLabel.anchorPoint = ccp(0.5, 0.3);
		textLabel.scale = .5;
		[subItem addChild:textLabel z:99];	
		
		[menu addChild:subItem z:1 tag:1];
		prevBTN = subItem;
		prevBTN.isEnabled = NO;
		subItem.position = ccp(-100, -120);
		dstPoint = subItem.position;
		offset = round(screenSize.width/2) + 150;
		id movebtn3 = [CCMoveBy actionWithDuration:2 position:ccp(dstPoint.x + offset,0)];
		id actionbtn3 = [CCEaseElasticOut actionWithAction:movebtn3 period:0.3f];
		
		subItem.position = ccp( dstPoint.x - offset, dstPoint.y);
		[subItem runAction:actionbtn3];
		//NSString *file = [[NSBundle mainBundle] pathForResource:@"levelinfo" ofType:@"plist"];
		levelManager = [OOOLevelManager sharedLevelManager];
		currentLevel = [levelManager getLevelProgressionIndex];
		previews = [levelManager getLevels];//[[NSMutableArray arrayWithContentsOfFile:file] retain];
		
		[self buildPreviewWithIndex: previewIndex];
		[self addChild:menu];
	}
	return self;
}	



-(void) goLevel: (CCMenuItemSprite*)sender
{
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	NSDictionary *userinfo = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithInt:previewIndex],@"level_ind",nil];
	[[NSNotificationCenter defaultCenter] 
			postNotification:[NSNotification 
					   notificationWithName:@"levelEntered" 
					   object:nil 
					   userInfo:userinfo]];
}


-(void) goNext: (CCMenuItemSprite*)sender
{
	if(previewIndex<([previews count]-1)){
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		previewIndex ++;
		[self buildPreviewWithIndex: previewIndex];
		prevBTN.isEnabled = YES;
		
	}
	if(previewIndex==[previews count]-1){
		nextBTN.isEnabled = NO;
	}
	if(previewIndex>currentLevel){
		playBTN.isEnabled =NO;
	}
}

-(void) goPrev: (CCMenuItemSprite*)sender
{
	//NSLog(@"sender: %@",sender);
	if(previewIndex>0){
		[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
		previewIndex --;
		[self buildPreviewWithIndex: previewIndex];
		nextBTN.isEnabled = YES;
	}
	if(previewIndex==0){
		prevBTN.isEnabled = NO;
	}
	if(previewIndex<=currentLevel){
		playBTN.isEnabled =YES;
	}
}


-(void) buildPreviewWithIndex: (uint) pIndex
{
	//NSLog(@"[self getChildByTag:99]:%@",[self getChildByTag:99]);
	if([self getChildByTag:100]!= nil){
		[self removeChild:[self getChildByTag:100] cleanup:YES];
	}
	if([self getChildByTag:99]!= nil){
		[self removeChild:[self getChildByTag:99] cleanup:YES];
	}
	if([self getChildByTag:98]!= nil){
		[self removeChild:[self getChildByTag:98] cleanup:YES];
	}
	
	if([self getChildByTag:97]!= nil){
		[self removeChild:[self getChildByTag:97] cleanup:YES];
	}
	
	if([self getChildByTag:96]!= nil){
		[self removeChild:[self getChildByTag:96] cleanup:YES];
	}
	
	if([self getChildByTag:95]!= nil){
		[self removeChild:[self getChildByTag:95] cleanup:YES];
	}
	//NSLog(@"preview index: %i", pIndex);
	
	//NSLog(@"level title: %@",previews);
	//NSLog(@"level title: %@",[previews objectAtIndex:pIndex]);
	NSMutableDictionary *preview = [previews objectAtIndex:pIndex];
	//NSLog(@"level title: %s", [preview objectForKey:@"levelTitle"]);
	
		
	NSString *scoreString = nil;
	NSString *picname = [preview objectForKey:@"pic"];
	if(picname==nil){
		picname = @"noImage.png";
	}
	CCSprite *pic = [CCSprite spriteWithFile:picname];
	[self addChild:pic z:1 tag:98];
	//pic.scale = .5;
	//pic.rotation = -90;
	pic.position = ccp(140,160);
	if(pIndex<=currentLevel){
		if(pIndex == 0 ){
			scoreString = @"Status: Played";
		}else{
			NSString *scoreTag = @"Hiscore: ";
			scoreString = [scoreTag stringByAppendingString:[[preview objectForKey:@"score"] stringValue]];
		}
		
	}else{
		scoreString = @"Status: LOCKED";
		CCSprite *lock = [CCSprite spriteWithFile:@"lock.png"];
		[self addChild:lock z:1 tag:96];
		lock.position = ccp(285, 217);
		
	}
	CCBitmapFontAtlas *scoreLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:scoreString fntFile:@"MarkerFelt_Brown.fnt"];
	scoreLabel.position = ccp(276 + .5*scoreLabel.contentSize.width/2 ,80);
	scoreLabel.anchorPoint = ccp(0.5, 0.3);
	scoreLabel.scale = .5 ;
	[self addChild:scoreLabel z:1 tag:97];
	
	CCBitmapFontAtlas *titleLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:[preview objectForKey:@"levelTitle"] fntFile:@"marker_felt2.fnt"];
	//NSLog(@"contentsize.width: %3.3f",titleLabel.contentSize.width);
	titleLabel.position = ccp(20 + .7*titleLabel.contentSize.width/2 ,260);
	titleLabel.anchorPoint = ccp(0.5, 0.3);
	titleLabel.scale = .7 ;
	[self addChild:titleLabel z:1 tag:99];
	
	NSString *levelNumber = [NSString stringWithFormat:@"Level: %i",(pIndex + 1)];
	CCBitmapFontAtlas *levelLabel = [CCBitmapFontAtlas bitmapFontAtlasWithString:levelNumber fntFile:@"MarkerFelt_Brown.fnt"];
	levelLabel.position = ccp(276 + .5*levelLabel.contentSize.width/2 ,143);
	levelLabel.anchorPoint = ccp(0.5, 0.3);
	levelLabel.scale = .5 ;
	[self addChild:levelLabel z:1 tag:100];
	
	
	
	CCSpriteSheet *sheet = [CCSpriteSheet spriteSheetWithFile:@"level_map.png" capacity:150];
	[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"level_map.plist"];
	[self addChild:sheet z:1 tag:95];
	
	CCSprite *starInd;
	int numStars = [[OOOLevelManager sharedLevelManager] getStarsForScore: [[preview objectForKey:@"score"] intValue]]; 
	//NSLog(@"numStars: %i",numStars );
	if(numStars ==1){
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0003.png"];
		starInd.position = ccp(295.0, 120.0);
	}else if(numStars ==2){
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0002.png"];
		starInd.position = ccp(314.0, 120.0);
	}else{
		starInd = [CCSprite spriteWithSpriteFrameName:@"starindicator0001.png"];
		starInd.position = ccp(332.0, 121.0);
	}
	//NSLog(@"num stars --> %@",[[OOOLevelManager sharedLevelManager] getNumStarsForPrevLevel]);
	[sheet addChild:starInd];
	
	//starInd.scale=.5;
	
	
}

-(void) goBack: (id)sender
{
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu scene]]];
}





- (void)dealloc {
	//NSLog(@"deallocing howtoplay");
    [super dealloc];
}


@end
