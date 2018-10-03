//
//  GameSprite.m
//  oneonone
//
//  Created by johan ten broeke on 2/23/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import "OOOGameSprite.h"
#import "Box2D.h"



@implementation OOOGameSprite


-(id)initWithSheet: (CCSpriteSheet *)_sheet andName:(NSString *)_name andKeyFrame:(NSString *)frame{
	//NSLog(@"---> frame name %@",frame);
	//NSLog(@"---> name %@",_name);
	if( (self=[super init])) {
		name = _name;
		sheet = _sheet;
		_obeyPhysics = YES;
		[self initWithSpriteFrameName:frame];
		
	}
	return self;

}

-(b2Joint *)getJointByName: (NSString *)_name{
	for (b2JointEdge* jointEdge = myBody->GetJointList(); jointEdge != NULL; jointEdge = jointEdge->next)
	{
		b2Joint* targetJoint = jointEdge->joint;
		if ([_name isEqualToString: (NSString *)targetJoint->GetUserData()]){
			return targetJoint;
		}		
	}
	return nil;
}

-(void)destroyJointByName: (NSString *)_name{
	b2Joint *jointToDestruct = [self getJointByName:_name];
	if (jointToDestruct) {
		NSDictionary *user_info = [NSDictionary dictionaryWithObject:[NSValue valueWithPointer:jointToDestruct] forKey:@"joint"];
		[[NSNotificationCenter defaultCenter] 
		 postNotification:[NSNotification 
						   notificationWithName:@"destroyJoint" 
						   object:nil 
						   userInfo:user_info]];
	}
}

-(void)update{
	if (_obeyPhysics) {
		self.position = CGPointMake( myBody->GetPosition().x * PTM_RATIO, myBody->GetPosition().y * PTM_RATIO);
		self.rotation = -1 * CC_RADIANS_TO_DEGREES(myBody->GetAngle());
	}
}

-(void)obeyPhysics:(BOOL)_bool{
	_obeyPhysics = _bool;
}

-(void) setB2Body: (b2Body *)body{
	myBody = body;
	//NSLog(@"pointer to b2Body : %p",myBody);
}

-(b2Body *)getB2Body{
	return myBody;
}

-(void)setClassName:(NSString *)n{
	className = n;
	[className retain];
}

-(NSString *)getClassName{
	return className;
}

-(NSString *)getName{
	return name;
}

- (void)setWidth:(float)width
{
	float newScale = (width * self.scaleX)/self.contentSize.width;
	self.scaleX = newScale;
}

- (void)setHeight:(float)height
{
	float newScale = (height * self.scaleY)/self.contentSize.height;
	self.scaleY = newScale;
}

-(void)playFrames:(NSArray *)frames loop:(BOOL)_loop target:(id)obj callback:(SEL)cb{
	NSMutableArray *animFrames = [NSMutableArray array];
	int l = [frames count];
	for (int i=0; i<l; i++){
		NSString *frame_name = [frames objectAtIndex:i]; 
		CCSpriteFrame *frame = [[CCSpriteFrameCache sharedSpriteFrameCache] spriteFrameByName:frame_name];
		[animFrames addObject:frame];
	}
	CCAnimation *anim = [[CCAnimation animationWithName:@"jump_to" delay:0.1f frames:animFrames] retain];
	if (_loop){
		[self runAction:[CCRepeatForever actionWithAction: [CCAnimate actionWithAnimation:anim restoreOriginalFrame:YES]]];
	}else{
		id _anim = [CCAnimate actionWithAnimation:anim restoreOriginalFrame:NO];
		id seq = [CCSequence actions:_anim, [CCCallFunc actionWithTarget:obj selector:cb], nil];
		[self runAction:seq];
	}
	[anim release];
	
}

-(void)stop{
	[self stopAllActions];
}

-(void)gotoAndStop:(NSString *)frame_name{
	CCSpriteFrame *frame = [[CCSpriteFrameCache sharedSpriteFrameCache] spriteFrameByName:frame_name];
	NSArray *animFrames = [NSArray arrayWithObject:frame];
	CCAnimation *anim = [[CCAnimation animationWithName:@"jump_to" delay:0.1f frames:animFrames] retain];
	[self runAction:[CCAnimate actionWithAnimation:anim restoreOriginalFrame:NO]];
	[anim release];
}

-(NSArray*)buildSequence:(NSString *)frame_name{
	int arrayCount = [keyframes count];
	BOOL found = NO;
	NSMutableArray *animFrames = [NSMutableArray array];
	NSMutableArray *skippedFrames = [NSMutableArray array];
	for (int i = 0; i < arrayCount; i++) {
		if ([[keyframes objectAtIndex:i] isEqualToString:frame_name]){
			found = YES;
		}
		if (found){
			[animFrames addObject:[keyframes objectAtIndex:i]];
		}else {
			[skippedFrames addObject:[keyframes objectAtIndex:i]];
		}
	}
	NSArray *finalFramesNames = [animFrames arrayByAddingObjectsFromArray:skippedFrames];
	int frameCount = [finalFramesNames count];
	NSMutableArray *finalFrames = [NSMutableArray array];
	for(int j = 0; j < frameCount; j++) {
		CCSpriteFrame *frame = [[CCSpriteFrameCache sharedSpriteFrameCache] 
								spriteFrameByName:[finalFramesNames objectAtIndex:j]];
		[finalFrames addObject:frame];
	}
	return finalFrames;
}

-(void)destroy{
	//NSLog(@"destroy called! %@",self);
	[self destroyPhysics];
	[[self parent] removeChild:self cleanup:NO];
}

-(void)destroyPhysics{
	NSDictionary *user_info = [NSDictionary dictionaryWithObject:[NSValue valueWithPointer:myBody] forKey:@"body"];
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"destroyPhysics" 
					   object:nil 
					   userInfo:user_info]];
	//NSLog(@"destroyPhysics called! %@",self);
}

-(void)gotoAndPlay:(NSString *)frame_name loop:(BOOL)_loop{
	NSArray *frames = [self buildSequence:frame_name];
	CCAnimation *anim = [[CCAnimation animationWithName:@"jump_to" delay:0.1f frames:frames] retain];
	if (_loop){
		[self runAction:[CCRepeatForever actionWithAction: [CCAnimate actionWithAnimation:anim restoreOriginalFrame:YES]]];
	}else{
		[self runAction:[CCAnimate actionWithAnimation:anim restoreOriginalFrame:NO]];
	}
	[anim release];
}

-(void)gotoAndPlay:(NSString *)frame_name target:(id)obj callback:(SEL)cb{
	NSArray *frames = [self buildSequence:frame_name];
	CCAnimation *anim = [[CCAnimation animationWithName:@"jump_to" delay:0.1f frames:frames] retain];
	id _anim = [CCAnimate actionWithAnimation:anim restoreOriginalFrame:NO];
	id seq = [CCSequence actions:_anim, [CCCallFunc actionWithTarget:obj selector:cb], nil];
	[self runAction:seq];
	[anim release];
}

-(void)setKeyFrames:(NSArray *)_keyframes{
	keyframes = _keyframes;
	[keyframes retain];
}


- (void) dealloc
{
	[keyframes release];
	[className release];
	[super dealloc];
}


@end
