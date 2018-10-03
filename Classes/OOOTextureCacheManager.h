//
//  OOOTextureCacheManager.h
//  oneonone_stripped
//
//  Created by johan ten broeke on 7/27/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>


@interface OOOTextureCacheManager : NSObject {
	NSMutableDictionary *atlasNames;
	NSString *currentTexture;
}
+ (OOOTextureCacheManager *)sharedTextureCacheManager;
- (void)addAtlas:(NSString *)atlas;

@end
