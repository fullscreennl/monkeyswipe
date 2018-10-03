//
//  OOOGameModel.h
//  oneonone
//
//  Created by Johan ten Broeke on 2/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#import "Box2D.h"
#import "OOOGameSprite.h"
#import "GLES-Render.h"
#import "OOOContactListener.h"


@interface OOOGameModel : NSObject {
	b2World* world;
	b2Body* groundBody;
	GLESDebugDraw *m_debugDraw;
	int stepcounter;
	BOOL allowImpulse;
	NSArray *impulse_arr;
	OOOContactListener* cl;
	NSMutableDictionary *contact_dict;
	NSMutableArray *deadBodyList;
	NSMutableArray *deadJointList;
}

-(void) createWorld;
-(void) onGameLoop;
-(void) createDistJoint: (NSDictionary *) joint_dict;
-(void) createRevJoint: (NSDictionary *) joint_dict;
-(void) createPrismJoint: (NSDictionary *) joint_dict;
-(b2Body *)createCompoundPhysicsWithSpriteAttached:(OOOGameSprite *)sprite andDict:(NSDictionary *)dict;
-(void) registerContacts:(NSArray *)contacts;
-(void) onEnterTransitionDidFinish;
-(b2World *) getWorld;
@end
