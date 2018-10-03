//
//  OOOTextureCacheManager.m
//  oneonone_stripped
//
//  Created by johan ten broeke on 7/27/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#define DOODLE_SHEET @"tut_textures.plist"
#define VECTOR_SHEET @"test_texture.plist"

#import "OOOTextureCacheManager.h"
#import "cocos2d.h"


@implementation OOOTextureCacheManager

static OOOTextureCacheManager *sharedOOOTextureCacheManager_=nil;

+ (OOOTextureCacheManager *)sharedTextureCacheManager
{
	if (!sharedOOOTextureCacheManager_)
		sharedOOOTextureCacheManager_ = [[OOOTextureCacheManager alloc] init];
	
	return sharedOOOTextureCacheManager_;
}

-(id) init
{
	if( (self=[super init])) {
		atlasNames = [[NSMutableDictionary alloc] init];
	}
	return self;
}

-(void)addAtlas:(NSString *)atlas{
	//[atlas retain];
	if ([atlas isEqualToString:DOODLE_SHEET] || [atlas isEqualToString:VECTOR_SHEET] ) {
		if (![currentTexture isEqualToString:atlas]) {
			[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:atlas];
			[atlasNames setObject:[NSNumber numberWithInt:YES] forKey:atlas];
			[currentTexture release];
			currentTexture = atlas;
			[currentTexture retain];
			//NSLog(@"major texture switch alert!!!!");
		}
	}
	
	
	if(! [atlasNames objectForKey:atlas]){
		[atlasNames setObject:[NSNumber numberWithInt:YES] forKey:atlas];
		[[CCSpriteFrameCache sharedSpriteFrameCache] addSpriteFramesWithFile:atlas];
	}
	//NSLog(@"atlasNames Dictionary: %@",atlasNames);
	//NSLog(@"currentTexture: %@",currentTexture);
	//[atlas release];
}

-(void)dealloc{
	[super dealloc];
	
	[atlasNames release];
}


@end
