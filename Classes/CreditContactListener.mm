//
//  ContactListener.mm
//  BeetleBeat
//
//  Created by Jeroen Goor van on 2/22/10.
//  Copyright 2010 Fullscreen. All rights reserved.
//

#import "CreditContactListener.h"
#import "Box2D.h"
#import "cocos2d.h"
#import "b2Contact.h"
#import <Foundation/Foundation.h>
#import "SimpleAudioEngine.h"

// Implement contact listener.
CreditContactListener::CreditContactListener(){};

void CreditContactListener::BeginContact(b2Contact* contact)
{
	b2Fixture* fixtureA = contact->GetFixtureA();
	CCSprite* sprite = (CCSprite*)fixtureA->GetBody()->GetUserData();

	b2Fixture* fixtureB = contact->GetFixtureB();
	CCSprite* sprite2 = (CCSprite*)fixtureB->GetBody()->GetUserData();
	if((sprite.tag==99 and sprite2.tag==66) or (sprite.tag==66 and sprite2.tag==99) ){
		//touch jeroen
		//[[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName: @"onPointPlayer" object:nil userInfo:nil]];
		float rnd = CCRANDOM_0_1();
		if(rnd<.33){
			[[SimpleAudioEngine sharedEngine] playEffect:@"jeroen_au1.wav"];
		}else if(rnd >.33 and rnd < .66){
			[[SimpleAudioEngine sharedEngine] playEffect:@"jeroen_au2.wav"];
		}else{
			[[SimpleAudioEngine sharedEngine] playEffect:@"jeroen_au3.wav"];
		}
		[[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName: @"onHitJeroen" object:nil userInfo:nil]];
	}else if ((sprite.tag==99 and sprite2.tag==55) or (sprite.tag==55 and sprite2.tag==99)) {
		//touch johan
		//[[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName: @"onPointBot" object:nil userInfo:nil]];
		float rnd = CCRANDOM_0_1();
		if(rnd<.33){
			[[SimpleAudioEngine sharedEngine] playEffect:@"johan_au1.wav"];
		}else if(rnd >.33 and rnd < .66){
			[[SimpleAudioEngine sharedEngine] playEffect:@"johan_au2.wav"];
		}else{
			[[SimpleAudioEngine sharedEngine] playEffect:@"johan_au3.wav"];
		}
		[[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName: @"onHitJohan" object:nil userInfo:nil]];
	}else if(sprite.tag==99 or sprite2.tag==99){
		[[SimpleAudioEngine sharedEngine] playEffect:@"sfx_bounce.wav"];
		[[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName: @"onHitBeetle" object:nil userInfo:nil]];
	}
	//NSDictionary* dict = [NSDictionary dictionaryWithObjectsAndKeys: sprite,@"sprite1",sprite2 ,@"sprite2",nil];
	//[[NSNotificationCenter defaultCenter] postNotification:[NSNotification notificationWithName: @"onContact" object:nil userInfo:dict]];
	
}



// Implement contact listener.
void CreditContactListener::EndContact(b2Contact* contact)
{
	//NSLog(@"endcontact");

}