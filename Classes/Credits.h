//
//  Beat_the_Beetle.h
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/19/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

// When you import this file, you import all the cocos2d classes
#import "cocos2d.h"
#import "Box2D.h"
#import "GLES-Render.h"
#import "CreditContactListener.h"

// HelloWorld Layer
@interface Credits : CCLayer
{
	
	b2World *world;
	
	GLESDebugDraw *m_debugDraw;
	b2Body *johan; 
	b2Body *jeroen;
	b2Body *groundBody;
	b2Body *ballBody;
	int jeroenHits;
	int johanHits;
	CCSprite *ballSprite;
	CCSprite *johanSprite;
	CCSprite *jeroenSprite;
	CCAnimation *hitAnimation;
	//CCAnimation *looseAnimation;
	//CCAnimation *winAnimation;
	///CCAnimation *botLooseAnimation;
	//CCAnimation *botWinAnimation;
	//CCAnimation *posingAnimation;
	b2BodyDef ballBodyDef;
	//b2BodyDef jeroenBodyDef;
	//b2BodyDef johanBodyDef;
	BOOL allowImpulse;
	BOOL gameOver;
	//const b2MassData massData;
	NSNumber* scorePlayer;
	NSNumber* scoreBot;
	int maxSpeed;
	float32 speed;
	CreditContactListener* _contactLister;
}



// returns a Scene that contains the HelloWorld as the only child
+(id) scene;

// adds a new sprite at a given coordinate
-(void) addNewSpriteWithCoords:(CGPoint)p withName:(NSString*)name_;
-(void) addNewBallSpriteWithCoords:(CGPoint)p;
-(void) slamBall:(b2Body *)ball;
-(void)goHome:(id)sender;
@end
