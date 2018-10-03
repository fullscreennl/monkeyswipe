//
//  ContactListener.h
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/22/10.
//  Copyright 2010 Fullscreen. All rights reserved.
//

#import "CreditContactListener.h"
#import "Box2D.h"
#import "b2Contact.h"

class CreditContactListener : public b2ContactListener
{
public:
	CreditContactListener();
	
	void* userData; /// Use this to store application specific body data.
	void BeginContact(b2Contact* contact);
	void EndContact(b2Contact* contact);
};