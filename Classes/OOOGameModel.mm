//
//  OOOGameModel.m
//  oneonone
//
//  Created by Johan ten Broeke on 2/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//
#define PTM_RATIO 32
#define SCREEEN_WIDTH 480
#define SCREEEN_HEIGHT 320

#import "OOOGameModel.h"
#import "OOONotificationNames.h"
#import "cocos2d.h"
#import "OOOContactListener.h"

@implementation OOOGameModel


-(id) init
{
	if( (self=[super init])) {
		[self createWorld];
	}	
	return self;
}



-(void) createWorld
{
	stepcounter = 0;
	
	// Define the gravity vector.
	b2Vec2 gravity;
	gravity.Set(0.0f, -10.0f);
	
	// Do we want to let bodies sleep?
	// This will speed up the physics simulation
	bool doSleep = true;
	
	deadBodyList = [[NSMutableArray alloc] init];
	deadJointList = [[NSMutableArray alloc] init];
	
	// Construct a world object, which will hold and simulate the rigid bodies.
	world = new b2World(gravity, doSleep);
	
	world->SetContinuousPhysics(true);
	
	// Debug Draw functions
	m_debugDraw = new GLESDebugDraw( PTM_RATIO );
	world->SetDebugDraw(m_debugDraw);
	
	uint32 flags = 0;
	flags += b2DebugDraw::e_shapeBit;
	flags += b2DebugDraw::e_jointBit;
	//		flags += b2DebugDraw::e_aabbBit;
	//		flags += b2DebugDraw::e_pairBit;
	//		flags += b2DebugDraw::e_centerOfMassBit;
	m_debugDraw->SetFlags(flags);		
	
	
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
	groundBox.SetAsEdge(b2Vec2(0,0), b2Vec2(SCREEEN_WIDTH/PTM_RATIO,0));
	groundBody->CreateFixture(&groundBox);
	
	// top
	groundBox.SetAsEdge(b2Vec2(0,SCREEEN_HEIGHT/PTM_RATIO), b2Vec2(SCREEEN_WIDTH/PTM_RATIO,SCREEEN_HEIGHT/PTM_RATIO));
	groundBody->CreateFixture(&groundBox);
	
	// left
	groundBox.SetAsEdge(b2Vec2(0,SCREEEN_HEIGHT/PTM_RATIO), b2Vec2(0,0));
	groundBody->CreateFixture(&groundBox);
	
	// right
	groundBox.SetAsEdge(b2Vec2(SCREEEN_WIDTH/PTM_RATIO,SCREEEN_HEIGHT/PTM_RATIO), b2Vec2(SCREEEN_WIDTH/PTM_RATIO,0));
	groundBody->CreateFixture(&groundBox);

	
}

-(b2World *)getWorld{
	return world;
}

-(void)onEnterTransitionDidFinish{
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onBodyDestructionRequested:) 
												 name:@"destroyPhysics" 
											   object:nil];
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onJointDestructionRequested:) 
												 name:@"destroyJoint" 
											   object:nil];
	
	
	[[NSNotificationCenter defaultCenter] addObserver:self 
											 selector:@selector(onExplosionRequested:) 
												 name:@"explodeBody" 
											   object:nil];
	
}

-(void)onExplosionRequested: (NSNotification *)note{
	
	float maxDistance = 10; 
	float power = 7;
	float distance; 
	
	b2Body *exploding_body = (b2Body *)[[[note userInfo] objectForKey:@"body"] pointerValue];

	b2Vec2 point(exploding_body->GetPosition().x, exploding_body->GetPosition().y);
	for (b2Body* b = world->GetBodyList(); b; b = b->GetNext()){
		distance = b2Distance(exploding_body->GetPosition(), b->GetPosition());
		if(distance < maxDistance){ 
			
			float x_component = ((b->GetPosition().x - exploding_body->GetPosition().x) / distance) * (maxDistance - distance)*power;
			float y_component = ((b->GetPosition().y - exploding_body->GetPosition().y) / distance) * (maxDistance - distance)*power;
				
			if (b != exploding_body){
				b->ApplyImpulse(b2Vec2( x_component, 
									    y_component), 
									    exploding_body->GetPosition());
			}
		}
	}
}

-(void)onJointDestructionRequested: (NSNotification *)note{
	//NSLog(@"onJointDestructionRequested called! %@",self);
	NSValue *obj = [[note userInfo] objectForKey:@"joint"];
	if(![deadJointList containsObject:obj]){
		[deadJointList addObject:obj];
	}
}

-(void)cleanDeadJoints{
	while([deadJointList count] > 0){
		b2Joint *deadJoint = (b2Joint *)[[deadJointList objectAtIndex:0] pointerValue];
		[deadJointList removeObjectAtIndex:0];
		world->DestroyJoint(deadJoint);
	}
}


-(void)onBodyDestructionRequested: (NSNotification *)note{
	NSValue *obj = [[note userInfo] objectForKey:@"body"];
	if(![deadBodyList containsObject:obj]){
		[deadBodyList addObject:obj];
	}
}

-(void)cleanDeadBodies{
	while([deadBodyList count] > 0){
		b2Body *deadBody = (b2Body *)[[deadBodyList objectAtIndex:0] pointerValue];
		[deadBodyList removeObjectAtIndex:0];
		world->DestroyBody(deadBody);
	}
}

-(void)registerContacts:(NSArray *)contacts{
	cl = new OOOContactListener();
	int arrayCount = [contacts count];
	contact_dict = [[NSMutableDictionary dictionary] retain];
	for (int i = 0; i < arrayCount; i++) {
		NSString *evt = [[contacts objectAtIndex:i] objectForKey:@"eventName"];
		NSString *name_1 = [[contacts objectAtIndex:i] objectForKey:@"sprite1"];
		NSString *name_2 = [[contacts objectAtIndex:i] objectForKey:@"sprite2"];
		NSString *entry_1 = [name_1 stringByAppendingString:name_2];
		NSString *entry_2 = [name_2 stringByAppendingString:name_1];
		[contact_dict setObject: evt  forKey:entry_1];
		[contact_dict setObject: evt  forKey:entry_2];
	}
	//NSLog(@"contac dict %@",contact_dict);
	cl->SetContacts(contact_dict);
	world->SetContactListener(cl);
}

-(b2Body *) getBodyBySpriteName: (NSString *) name{
	for (b2Body* b = world->GetBodyList(); b; b = b->GetNext()){
		if (b->GetUserData() != NULL) {
			OOOGameSprite *myActor = (OOOGameSprite*)b->GetUserData();
			if ([myActor getName] == name) {
				return b;
			}
		}	
	}
	return nil;
}

-(void) createPrismJoint: (NSDictionary *) joint_dict{
	
	NSString * body1 = [joint_dict objectForKey:@"body1"];
	
	float mspeed = [[joint_dict objectForKey:@"motorSpeed"] floatValue];
	float mtorque = [[joint_dict objectForKey:@"maxMotorTorque"] floatValue];
	bool enablemotor = [[joint_dict objectForKey:@"enableMotor"] boolValue];
	float lower_ang = [[joint_dict objectForKey:@"lowerTranslation"] floatValue];
	float upper_ang = [[joint_dict objectForKey:@"upperTranslation"] floatValue];
	float xdir = [[joint_dict objectForKey:@"xdir"] floatValue];
	float ydir = [[joint_dict objectForKey:@"ydir"] floatValue];

	bool limit = [[joint_dict objectForKey:@"enableLimit"] boolValue];
	
	b2PrismaticJointDef pjd;
	
	b2Body * _b1 = [self getBodyBySpriteName:body1];
	
	pjd.Initialize( groundBody, _b1, b2Vec2(_b1->GetPosition().x , _b1->GetPosition().y), b2Vec2(xdir, ydir));
	pjd.motorSpeed = mspeed;
	pjd.maxMotorForce = mtorque;
	pjd.enableMotor = enablemotor ;
	pjd.lowerTranslation = lower_ang/PTM_RATIO;
	pjd.upperTranslation = upper_ang/PTM_RATIO;
	pjd.enableLimit = limit;
	
	world->CreateJoint(&pjd);
	
}

-(void) createRevJoint: (NSDictionary *) joint_dict{

	NSString * body1 = [joint_dict objectForKey:@"body1"];
	NSString * body2 = [joint_dict objectForKey:@"body2"];
	
	float mspeed = [[joint_dict objectForKey:@"motorSpeed"] floatValue];
	float mtorque = [[joint_dict objectForKey:@"maxMotorTorque"] floatValue];
	bool enablemotor = [[joint_dict objectForKey:@"enableMotor"] boolValue];
	float lower_ang = [[joint_dict objectForKey:@"lowerAngle"] floatValue];
	float upper_ang = [[joint_dict objectForKey:@"upperAngle"] floatValue];
	bool limit = [[joint_dict objectForKey:@"enableLimit"] boolValue];
	bool collideConnected = [[joint_dict objectForKey:@"collideConnected"] boolValue];
	
	NSString *user_data = [joint_dict objectForKey:@"userData"];

	b2RevoluteJointDef rjd;
	
	b2Body * _b1 = [self getBodyBySpriteName:body1];
	b2Body * _b2 = [self getBodyBySpriteName:body2];
	

	rjd.Initialize( _b1, _b2, b2Vec2(_b1->GetPosition().x , _b1->GetPosition().y));
	rjd.motorSpeed = mspeed;
	rjd.maxMotorTorque = mtorque;
	rjd.enableMotor = enablemotor ;
	rjd.lowerAngle = lower_ang;
	rjd.upperAngle = upper_ang;
	rjd.enableLimit = limit;
	rjd.collideConnected = collideConnected;
	
	b2Joint *joint = world->CreateJoint(&rjd);
	joint->SetUserData(user_data);
}

-(void) createDistJoint: (NSDictionary *) joint_dict{

	NSString * body1 = [joint_dict objectForKey:@"body1"];
	NSString * body2 = [joint_dict objectForKey:@"body2"];
	
	float freq = [[joint_dict objectForKey:@"frequencyHz"] floatValue];
	float dmp = [[joint_dict objectForKey:@"dampingRatio"] floatValue];
	
	float b1_Xoffset = [[joint_dict objectForKey:@"b1_Xoffset"] floatValue]/PTM_RATIO;
	float b1_Yoffset = [[joint_dict objectForKey:@"b1_Yoffset"] floatValue]/PTM_RATIO;
	float b2_Xoffset = [[joint_dict objectForKey:@"b2_Xoffset"] floatValue]/PTM_RATIO;
	float b2_Yoffset = [[joint_dict objectForKey:@"b2_Yoffset"] floatValue]/PTM_RATIO;
	
	//NSLog(@"x offset %f",b1_Xoffset);
	
	b2DistanceJointDef djd;
	
	b2Body * _b1 = [self getBodyBySpriteName:body1];
	b2Body * _b2 = [self getBodyBySpriteName:body2];
	
	
	djd.dampingRatio = dmp;
	djd.frequencyHz = freq;
	
	djd.Initialize(_b1, _b2, 
				   b2Vec2(_b1->GetPosition().x + b1_Xoffset, _b1->GetPosition().y + b1_Yoffset) ,
				   b2Vec2(_b2->GetPosition().x + b2_Xoffset, _b2->GetPosition().y + b2_Yoffset));
	
	world->CreateJoint(&djd);
	
}

-(b2Body *)createCompoundPhysicsWithSpriteAttached:(OOOGameSprite *)sprite andDict:(NSDictionary *)dict{
	
	float x = [[[dict objectForKey:@"body"] objectForKey:@"x"]floatValue];
	float y = [[[dict objectForKey:@"body"] objectForKey:@"y"]floatValue];
	float degAngle = [[[dict objectForKey:@"body"] objectForKey:@"angle"]floatValue];
	
	// Define the body.
	b2BodyDef bodyDef;
	if ([[dict objectForKey:@"body"] objectForKey:@"static"] and [[[dict objectForKey:@"body"] objectForKey:@"static"] boolValue] == YES){
		bodyDef.type = b2_staticBody;
	}else{
		bodyDef.type = b2_dynamicBody;
	}
	
	bodyDef.position.Set(x/PTM_RATIO, y/PTM_RATIO);
	bodyDef.angle = CC_DEGREES_TO_RADIANS(degAngle);
	//bodyDef.angle = (degAngle*2*3.14)/360;
	bodyDef.userData = sprite;
	
	b2Body *body = world->CreateBody(&bodyDef);
	
	b2CircleShape circ;
	b2PolygonShape dynamicBox;
	
	// Define the dynamic body fixture.
	b2FixtureDef fixtureDef;
	
	NSArray *shapes = [dict objectForKey:@"shapes"];

	int arrayCount = [shapes count];
	for (int i = 0; i < arrayCount; i++) {
		
		NSDictionary* shape_dict = [shapes objectAtIndex:i];
		
		float f = [[shape_dict objectForKey:@"friction"] floatValue];
		float d = [[shape_dict objectForKey:@"density"] floatValue];
		float r = [[shape_dict objectForKey:@"restitution"] floatValue];
		
		float w = [[shape_dict objectForKey:@"width"] floatValue];
		float h = [[shape_dict objectForKey:@"height"] floatValue];
		
		float xpos = [[shape_dict objectForKey:@"x"] floatValue];
		float ypos = [[shape_dict objectForKey:@"y"] floatValue];
		
		NSString *userData = [shape_dict objectForKey:@"userData"];
		//NSString *userData = [[shape_dict objectForKey:@"userData"] retain];
		
		NSString *sprite_type = [shape_dict objectForKey:@"type"];
		
		if ([sprite_type isEqual:@"circ"]) {
			circ.m_radius = w/PTM_RATIO/2;
			circ.m_p.Set(xpos/PTM_RATIO,ypos/PTM_RATIO);
			fixtureDef.shape = &circ;
		}else if ([sprite_type isEqual:@"rect"]) {
			dynamicBox.SetAsBox(w/PTM_RATIO/2, h/PTM_RATIO/2, b2Vec2(xpos/PTM_RATIO,ypos/PTM_RATIO), 0.0f);
			fixtureDef.shape = &dynamicBox;
		}else if ([sprite_type isEqual:@"poly"]) {
			NSString *points_str = [shape_dict objectForKey:@"points_CCW"];
			NSArray *points_arr = [points_str componentsSeparatedByString:@"#"];
			int c = [points_arr count];
			b2Vec2 vertices[c];
			for (int j = 0; j < c; j++) {
				NSArray* p = [[points_arr objectAtIndex:j] componentsSeparatedByString:@"|"];
				float _x = [[p objectAtIndex:0] floatValue];
				float _y = [[p objectAtIndex:1] floatValue];
				vertices[j].Set(_x/PTM_RATIO,_y/PTM_RATIO);
			}
			dynamicBox.Set(vertices,c);
			fixtureDef.shape = &dynamicBox;
		}
		
		fixtureDef.density = d;
		fixtureDef.friction = f;
		fixtureDef.restitution = r;
		fixtureDef.userData = userData;
		body->CreateFixture(&fixtureDef);
		
		//[userData release];
	}

	return body;
}

-(void) onGameLoop{
	
	int32 velocityIterations = 8;
	int32 positionIterations = 1;
	
	stepcounter ++;
		
	world->Step(1/60.0f, velocityIterations, positionIterations);
		
	for (b2Body* b = world->GetBodyList(); b; b = b->GetNext())
	{
		
		if (b->GetUserData() != NULL) {
			OOOGameSprite *myActor = (OOOGameSprite*)b->GetUserData();
			[myActor update];
		}	
	}
	[self cleanDeadBodies];
	[self cleanDeadJoints];
	
}

-(void)dealloc{
	[[NSNotificationCenter defaultCenter] removeObserver:self];
	
	[deadBodyList release];
	[deadJointList release];
	
	delete world;
	world = NULL;
	
	delete m_debugDraw;
	m_debugDraw = NULL;
	
	delete cl;
	cl = NULL;
	
	[contact_dict release];
	[super dealloc];
}


@end
