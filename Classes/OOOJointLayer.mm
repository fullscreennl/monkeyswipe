//
//  OOOJointLayer.mm
//  oneonone
//
//  Created by Johan ten Broeke on 3/21/10.
//  Copyright 2010 fullscreen.nl. All rights reserved.
//

#define PTM_RATIO 32

#import "OOOJointLayer.h"
#import "Box2D.h"



@implementation OOOJointLayer

+(id) layer
{
	OOOJointLayer *layer = [OOOJointLayer node];
	return layer;
}

// initialize your instance here
-(id) init
{
	if( (self=[super init])) {
		self.isTouchEnabled = NO;
	}
	return self;
}

-(void)setWorld:(b2World *)_world{
	world = _world;
}

-(void) draw
{
	for (b2Joint* b = world->GetJointList(); b; b = b->GetNext())
	{
		
		if(b->GetType() == 3){
			//b2Vec2 p1 = b->GetAnchorA().x;
			//b2Vec2 p2 = b->GetAnchorB().x;
           
			glEnable(GL_LINE_SMOOTH);
			
			// line: color, width, aliased
			// glLineWidth > 1 and GL_LINE_SMOOTH are not compatible
			// GL_SMOOTH_LINE_WIDTH_RANGE = (1,1) on iPhone
            glDisable(GL_TEXTURE_2D);
            glDisableClientState(GL_COLOR_ARRAY);
            glDisableClientState(GL_TEXTURE_COORD_ARRAY);
            GLfloat glVertices[] = {
                b->GetAnchorA().x * PTM_RATIO, b->GetAnchorA().y * PTM_RATIO,
                b->GetAnchorB().x * PTM_RATIO, b->GetAnchorB().y * PTM_RATIO
            };
            glVertexPointer(2, GL_FLOAT, 0, glVertices);
            glLineWidth( 2.0f );
            glColor4f(0,0,0,1.0f);
            glDrawArrays(GL_LINES, 0, 2);
            
            glEnable(GL_TEXTURE_2D);
            glEnableClientState(GL_COLOR_ARRAY);
            glEnableClientState(GL_TEXTURE_COORD_ARRAY);
//            glColor4ub(0,0,0,255);
//            ccDrawLine( ccp(b->GetAnchorA().x * PTM_RATIO, b->GetAnchorA().y * PTM_RATIO),
//                        ccp(b->GetAnchorB().x * PTM_RATIO, b->GetAnchorB().y * PTM_RATIO) );
            glDisable(GL_LINE_SMOOTH);
		}
	}
	
}


// on "dealloc" you need to release all your retained objects
- (void) dealloc
{
	//NSLog(@"OOODebugDrawLayer dealloced!!");
	[super dealloc];
}


@end
