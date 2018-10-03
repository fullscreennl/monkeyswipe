//
//  Beat_the_Beetle.m
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/19/10.
//  Copyright 2010 __Fullscreen__. All rights reserved.
//


#import "Credits.h"
#import "CreditContactListener.h"
#import "SimpleAudioEngine.h"
//#import "button.h"
#import "MainMenu.h"

//Pixel to metres ratio. Box2D uses metres as the unit for measurement.
//This ratio defines how many pixels correspond to 1 Box2D "metre"
//Box2D is optimized for objects of 1x1 metre therefore it makes sense
//to define the ratio so that your most common object type is 1x1 metre.
#define PTM_RATIO 26

// enums that will be used as tags
enum {
	
	kTagSpriteSheet = 1,
	kTagSpriteSheetBall = 99,
	kTagSpriteSheetPlayer= 3,
	kTagBotSpriteSheet=4,
	kTagSpriteSheetJeroen =66,
	kTagSpriteSheetJohan =55,	
	kTagPlayerSpriteSheet = 7,
	kTagAnimation1 = 1,
	kTagHomeBTN = 8,
	kTagBG = 5,
};


@implementation Credits

+(id) scene
{
	//NSLog(@"static scene called in beat the beetle");
	// 'scene' is an autorelease object.
	CCScene *scene = [CCScene node];

	// 'layer' is an autorelease object.
	Credits *layer = [Credits node];
	
	// add layer as a child to scene
	[scene addChild: layer];
	
	// return the scene
	return scene;
}

// initialize your instance here
-(id) init
{
	if( (self=[super init])) {
		//NSLog(@"init called in credit scene ");
		
		// enable touches
		self.isTouchEnabled = YES;
		// enable accelerometer
		self.isAccelerometerEnabled = YES;
		
		CGSize screenSize = [CCDirector sharedDirector].winSize;
		CCLOG(@"Screen width %0.2f screen height %0.2f",screenSize.width,screenSize.height);
		
		//setting up init stuff
		// Define the gravity vector.
		b2Vec2 gravity;
		gravity.Set(0.0f, -10.0f);
		
		allowImpulse = YES;
		
		// Do we want to let bodies sleep?
		// This will speed up the physics simulation
		bool doSleep = false;
		

		
		// Construct a world object, which will hold and simulate the rigid bodies.
		world = new b2World(gravity, doSleep);
		world->SetContinuousPhysics(true);
			
		// Debug Draw functions
		m_debugDraw = new GLESDebugDraw(PTM_RATIO);
		world->SetDebugDraw(m_debugDraw);
		
		uint32 flags = 0;
		flags += b2DebugDraw::e_shapeBit;
		flags += b2DebugDraw::e_jointBit;
		//		flags += b2DebugDraw::e_aabbBit;
		//		flags += b2DebugDraw::e_pairBit;
		flags += b2DebugDraw::e_centerOfMassBit;
		//m_debugDraw->SetFlags(flags);		
		
		_contactLister = new CreditContactListener();
		world->SetContactListener(_contactLister);
			
		// Define the ground body.
		b2BodyDef groundBodyDef;
		groundBodyDef.position.Set(0, 0); // bottom-left corner
		
		// Call the body factory which allocates memory for the ground body
		// from a pool and creates the ground box shape (also from a pool).
		// The body is also added to the world.
		groundBody = world->CreateBody(&groundBodyDef);
		
		// Define the ground box shape.
		b2PolygonShape groundBox;		
		
		// bottom
		groundBox.SetAsEdge(b2Vec2(0,0), b2Vec2(screenSize.width/PTM_RATIO,0));
		groundBody->CreateFixture(&groundBox);
		
		// top
		groundBox.SetAsEdge(b2Vec2(0,screenSize.height/PTM_RATIO), b2Vec2(screenSize.width/PTM_RATIO,screenSize.height/PTM_RATIO));
		groundBody->CreateFixture(&groundBox);
		
		// left
		groundBox.SetAsEdge(b2Vec2(0,screenSize.height/PTM_RATIO), b2Vec2(0,0));
		groundBody->CreateFixture(&groundBox);
		
		// right
		groundBox.SetAsEdge(b2Vec2(screenSize.width/PTM_RATIO,screenSize.height/PTM_RATIO), b2Vec2(screenSize.width/PTM_RATIO,0));
		groundBody->CreateFixture(&groundBox);
		
		//background image
		CCSprite *bg = [CCSprite spriteWithFile:@"creditBG.png"];
		bg.position =ccp(240.0f, 160.0f);
		[self addChild:bg z:0 tag:kTagBG];
		
		CCSprite *messageLabel = [CCSprite spriteWithFile:@"creditlist.png"];
		messageLabel.position = ccp(240.0f,-400.0f);
		[self addChild:messageLabel];
		
		id move = [CCMoveBy actionWithDuration:60.0f position:ccp(0.0f,997.0f)];
		id action = [CCEaseInOut actionWithAction:move rate:2];
		id move2 = [CCMoveBy actionWithDuration:0.1f position:ccp(0.0f,-997.0f)];
		id opchange = [CCFadeOut actionWithDuration:2.0f];
		id opchange2 = [CCFadeIn actionWithDuration:0.1f];
		id seq =[CCSequence actions: [CCDelayTime actionWithDuration: 2.5f],
										action,opchange,move2,opchange2,nil];	
		[messageLabel runAction:[CCRepeatForever actionWithAction:seq]]; 
		CCSprite *bg2 = [CCSprite spriteWithFile:@"creditBG4.png"];
		bg2.position =ccp(240.0f, 160.0f);
		[self addChild:bg2 z:0 tag:kTagBG];
		
		//Set up spriteAtlases for all textures
					
		CCSpriteSheet *playersheet = [CCSpriteSheet spriteSheetWithFile:@"credit_atlas_damagectrl.png" capacity:150];
		[self addChild:playersheet z:0 tag:kTagPlayerSpriteSheet];
		
		CCSpriteSheet *ballsheet =  [CCSpriteSheet spriteSheetWithFile:@"test_texture.png" capacity:150];
		[self addChild:ballsheet z:0 tag:kTagSpriteSheetBall];
				
		// left player
		CGPoint locationPlayer = CGPointMake(320.0f, 60.0f);
		locationPlayer = [[CCDirector sharedDirector] convertToGL: locationPlayer];
		[self addNewSpriteWithCoords: locationPlayer withName: @"johan"];
		//right player
		CGPoint locationBot = CGPointMake(320.0f, 420.0f);
		locationBot = [[CCDirector sharedDirector] convertToGL: locationBot];
		[self addNewSpriteWithCoords: locationBot withName: @"jeroen"];
				
		//ball
		CGPoint locationBall = CGPointMake(160.0f, 240.0f);
		locationBall = [[CCDirector sharedDirector] convertToGL: locationBall];
		[self addNewBallSpriteWithCoords:locationBall];
				
		//Button *btn = [Button buttonWithText:@"menu" andBGImage:@"homemenu_btn_green_left.png" andBGROImage:@"homemenu_btn_green_left_ro.png" andIcon:nil atPosition:ccp(990.0f, 60.0f) target:self selector:@selector(goHome:)];
		//id move4 = [CCMoveBy actionWithDuration:3 position:ccp(-550.0f,0.0f)];
		//id action4 = [CCEaseElasticOut actionWithAction:move4 period:0.3f];
				
		
		//[btn runAction:[CCSequence actions:[CCDelayTime actionWithDuration: 0.5f],action4,nil]];
		
		//[self addChild:btn z:1 tag:kTagHomeBTN];
		
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
												selector:@selector(goHome:)];	
		
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
		
		[self addChild:menu];
		
		[self schedule: @selector(tick:)];
		jeroenHits=0;
		johanHits=0;
		//[[SimpleAudioEngine sharedEngine] playBackgroundMusic:@"creditTheme.mp3"]; 
		//[[SimpleAudioEngine sharedEngine] setBackgroundMusicVolume:0.5f];
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onHitBeetle:) 
													 name:@"onHitBeetle" 
												   object:nil];
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onHitJeroen:) 
													 name:@"onHitJeroen" 
												   object:nil];
		[[NSNotificationCenter defaultCenter] addObserver:self 
												 selector:@selector(onHitJohan:) 
													 name:@"onHitJohan" 
												   object:nil];
		
	}
	return self;
}


-(void) draw
{
	// Default GL states: GL_TEXTURE_2D, GL_VERTEX_ARRAY, GL_COLOR_ARRAY, GL_TEXTURE_COORD_ARRAY
	// Needed states:  GL_VERTEX_ARRAY, 
	// Unneeded states: GL_TEXTURE_2D, GL_COLOR_ARRAY, GL_TEXTURE_COORD_ARRAY
	glDisable(GL_TEXTURE_2D);
	glDisableClientState(GL_COLOR_ARRAY);
	glDisableClientState(GL_TEXTURE_COORD_ARRAY);
	world->DrawDebugData();
	// restore default GL states
	glEnable(GL_TEXTURE_2D);
	glEnableClientState(GL_COLOR_ARRAY);
	glEnableClientState(GL_TEXTURE_COORD_ARRAY);
}

- (void)slamBall:(b2Body *)ball 
{
	b2Vec2 point(ball->GetPosition().x, ball->GetPosition().y);
	b2Vec2 impulse(5.0f, 0.0f);
	ball->ApplyImpulse(impulse,point);
}

-(void)addNewBallSpriteWithCoords:(CGPoint)p
{
	//CCLOG(@"Add ball sprite %0.2f x %0.2f",p.x,p.y);
	CCSpriteSheet *ballsheet =  (CCSpriteSheet*)[self getChildByTag:kTagSpriteSheetBall];
	[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"test_texture.plist"];
	CCSprite *sprite = [CCSprite spriteWithSpriteFrameName:@"hero_detailed.png"];	
	[ballsheet addChild:sprite z:0 tag:kTagSpriteSheetBall];
	sprite.position = ccp( p.x, p.y);
	sprite.scale = .5;
	
	NSMutableArray *animFrames = [NSMutableArray array];
	for(int i = 1; i < 7; i++) {
		
		CCSpriteFrame *frame = [[CCSpriteFrameCache sharedSpriteFrameCache] spriteFrameByName:[NSString stringWithFormat:@"frame_%02d.png",i]];
		if (frame!=nil) {
			[animFrames addObject:frame];
		}
	}
	
	hitAnimation = [[CCAnimation animationWithName:@"ball" delay:0.08f frames:animFrames] retain];
	
	//[sprite runAction:[CCRepeatForever actionWithAction: [CCAnimate actionWithAnimation:animation restoreOriginalFrame:NO] ]];
	//CCaction *action = [CCAction action];
	//[sprite runAction:[CCAnimate actionWithAnimation:hitAnimation restoreOriginalFrame:YES]];
	
	ballSprite = sprite;
	b2BodyDef bodyDef;
	bodyDef.type = b2_dynamicBody;
	bodyDef.position.Set(p.x/PTM_RATIO, p.y/PTM_RATIO);
	bodyDef.userData = sprite;

	b2Body *body = world->CreateBody(&bodyDef);
	ballBody = body;
	ballBodyDef = bodyDef;
	
	b2CircleShape dynamicBall;
	dynamicBall.m_radius = 28.0f/PTM_RATIO;
	
	b2FixtureDef fixtureDefBall;
	fixtureDefBall.shape = &dynamicBall;	
	fixtureDefBall.density = 1.0f;
	fixtureDefBall.restitution =1.0f;
	fixtureDefBall.friction = 0.3f;
	body->CreateFixture(&fixtureDefBall);
	[self slamBall:body];
}




-(void) addNewSpriteWithCoords:(CGPoint)p withName:(NSString *) name
{
	CCLOG(@"Add sprite %0.2f x %0.2f",p.x,p.y);
	CCSprite *sprite;
	if([name isEqualToString: @"jeroen"]){
		CCSpriteSheet *sheet = (CCSpriteSheet*) [self getChildByTag:kTagPlayerSpriteSheet];
		//[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:@"credit_atlas_damagectrl.plist"];
		sprite = [CCSprite spriteWithSpriteSheet:sheet rect:CGRectMake(128.0f, 0.0f, 128.0f, 128.0f)];
		jeroenSprite = sprite;
		[sheet addChild:sprite z:0 tag:kTagSpriteSheetJeroen];
		//[self addChild:sprite];
		sprite.position = ccp( p.x, p.y);
	}else{
		CCSpriteSheet *sheet = (CCSpriteSheet*) [self getChildByTag:kTagPlayerSpriteSheet];
		sprite = [CCSprite spriteWithSpriteSheet:sheet rect:CGRectMake(0.0f, 0.0f, 128.0f, 128.0f)];
		johanSprite =sprite;
		[sheet addChild:sprite z:0 tag:kTagSpriteSheetJohan];
		//[self addChild:sprite];
		sprite.position = ccp( p.x, p.y);
		
		
	}
	b2BodyDef bodyDef;
	bodyDef.type = b2_dynamicBody;
	bodyDef.position.Set(p.x/PTM_RATIO, p.y/PTM_RATIO);
	bodyDef.userData = sprite;
	
	b2Body *body = world->CreateBody(&bodyDef);
	if([name isEqualToString: @"jeroen"]){
		jeroen = body;
		//jeroenBodyDef = bodyDef;
	}else{
		johan = body;
		//johanBodyDef = bodyDef;
	}
	b2CircleShape dynamicBall;
	b2FixtureDef fixtureDef;
	dynamicBall.m_radius = 60.0f/PTM_RATIO;
	fixtureDef.shape = &dynamicBall;

	// Define the dynamic body fixture.
	fixtureDef.restitution = .9f;
	fixtureDef.density = 0.3f;
	fixtureDef.friction = 0.3f;
	fixtureDef.isSensor = NO;
	body->CreateFixture(&fixtureDef);
		
	
	//-----------------	
}


-(void)onHitBeetle:(NSNotification *)noti
{
	//[ballSprite runAction:[CCAnimate actionWithAnimation:hitAnimation restoreOriginalFrame:YES]];
	
}


-(void)onHitJeroen:(NSNotification *)noti
{
	if(jeroenHits<6 and speed>jeroenHits*5){
		jeroenHits += 1;
		//NSLog(@"jeroenHits: %i",jeroenHits);
		CCSpriteSheet *sheet = (CCSpriteSheet*) [self getChildByTag:kTagPlayerSpriteSheet];
		CCSprite *sprite =(CCSprite*) [sheet getChildByTag:kTagSpriteSheetJeroen];
		[sprite setTextureRect:CGRectMake(128.0f,jeroenHits*128.0f,128.0f,128.0f)];		
	}
	
}


-(void)onHitJohan:(NSNotification *)noti
{
	if( johanHits<6 and speed>5*johanHits){
		johanHits +=1;
		CCSpriteSheet *sheet = (CCSpriteSheet*) [self getChildByTag:kTagPlayerSpriteSheet];
		CCSprite *sprite =(CCSprite*)  [sheet getChildByTag:kTagSpriteSheetJohan];
		[sprite setTextureRect:CGRectMake(0.0f,johanHits*128.0f,128.0f,128.0f)];		
		//johanSprite = sprite;
	}
	
}


-(void) tick: (ccTime) dt
{
	//It is recommended that a fixed time step is used with Box2D for stability
	//of the simulation, however, we are using a variable time step here.
	//You need to make an informed choice, the following URL is useful
	//http://gafferongames.com/game-physics/fix-your-timestep/
	
	
		int32 velocityIterations = 8;
		int32 positionIterations = 1;
		world->Step(dt, velocityIterations, positionIterations);
	
	//Iterate over the bodies in the physics world
	for (b2Body* b = world->GetBodyList(); b; b = b->GetNext())
	{
		if (b->GetUserData() != NULL) {
			//Synchronize the AtlasSprites position and rotation with the corresponding body
			CCSprite *myActor = (CCSprite*)b->GetUserData();
			myActor.position = CGPointMake( b->GetPosition().x * PTM_RATIO, b->GetPosition().y * PTM_RATIO);
			myActor.rotation = -1 * CC_RADIANS_TO_DEGREES(b->GetAngle());
			CCSprite* sprite = (CCSprite*)b->GetUserData();
			if(sprite.tag == 99){
				//ball sprite
				b2Vec2 velocity = b->GetLinearVelocity();
				speed = velocity.Length();
			}
		}
		
		
	}
}


-(void)onExit
{
	//NSLog(@"Credit scene exited!");
	[super onExit];
	[[NSNotificationCenter defaultCenter] removeObserver:self];
	
}

-(void)onEnter
{
	[super onEnter];
	//NSLog(@"Credit scene entered!");
}


-(void)goHome:(id)sender
{
	[[SimpleAudioEngine sharedEngine] playEffect:@"btnTap.wav"];
	[[SimpleAudioEngine sharedEngine] stopBackgroundMusic];
	[[CCDirector sharedDirector] replaceScene:[CCFadeTransition transitionWithDuration:1.0 scene:[MainMenu node]]];
}



- (void)ccTouchesEnded:(NSSet *)touches withEvent:(UIEvent *)event
{
	b2Vec2 point(ballBody->GetPosition().x, ballBody->GetPosition().y);
	float Angle = ballBody->GetAngle() + .5*M_PI;
	//NSLog(@" angle ball: %2.2f",Angle);
	float nrX = cos(Angle);
	//NSLog(@" nrX ball: %2.2f",nrX);
	float nrY = sin(Angle);
	//NSLog(@" nrY ball: %2.2f",nrY);
	//nr = y/x;
	b2Vec2 impulse(730.0f*nrX/PTM_RATIO, 730.0f*nrY/PTM_RATIO);
	ballBody->ApplyImpulse(impulse,point);
}


- (void)accelerometer:(UIAccelerometer*)accelerometer didAccelerate:(UIAcceleration*)acceleration
{	
	static float prevX=0, prevY=0;
	
	//#define kFilterFactor 0.05f
	#define kFilterFactor 1.0f	// don't use filter. the code is here just as an example
	
	float accelX = (float) acceleration.x * kFilterFactor + (1- kFilterFactor)*prevX;
	float accelY = (float) acceleration.y * kFilterFactor + (1- kFilterFactor)*prevY;
	
	prevX = accelX;
	prevY = accelY;
	
	// accelerometer values are in "Portrait" mode. Change them to Landscape left
	// multiply the gravity by 10
	b2Vec2 gravity( -accelY * 10, accelX * 10);
	
	world->SetGravity( gravity );
}

// on "dealloc" you need to release all your retained objects
- (void) dealloc
{
	//NSLog(@"Credits dealloced!!");
	// in case you have something to dealloc, do it in this method
	delete _contactLister;
	_contactLister = NULL;
	
	delete world;
	world = NULL;
	
	delete m_debugDraw;
	[hitAnimation release];
	// don't forget to call "super dealloc"
	[super dealloc];
}
@end

