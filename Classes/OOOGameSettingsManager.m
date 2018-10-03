//
//  OOOGameSettingsManager.m
//  MonkeySwipe
//
//  Created by Jeroen Goor van on 3/31/10.
//  Copyright 2010 __MyCompanyName__. All rights reserved.
//

#import "OOOGameSettingsManager.h"


@implementation OOOGameSettingsManager

static OOOGameSettingsManager *_sharedManager = nil;

+ (OOOGameSettingsManager *)sharedManager
{
	if (!_sharedManager) {
		_sharedManager = [[self alloc] init];
	}
	return _sharedManager;
}

+(id)alloc
{
	NSAssert(_sharedManager == nil, @"Attempted to allocate a second instance of a singleton.");
	return [super alloc];
}

-(id) init
{
	if( (self=[super init])) {
		//settings = [NSMutableArray initialize];
	}
	return self;
}


-(void)setSettings:(NSMutableDictionary *) _settings
{
	[settings release];
	settings = [[NSMutableDictionary dictionaryWithDictionary: _settings] retain]; 
	//NSLog(@"settings dict: %p",settings);
}

-(void)dealloc{
	[settings release];
	[super dealloc];
}


-(NSMutableDictionary *)getSettings
{
	//BOOL soundFXMuted = [[settings objectForKey:@"soundFXMuted"] boolValue];
	//BOOL doodleStyle =[[settings objectForKey:@"doodleStyle"] boolValue];
	//NSLog(@"object for key soundFXMuted %i",soundFXMuted );
	//NSLog(@"object for key doodleStyle %i",doodleStyle );
	return settings; 
}



		
@end
