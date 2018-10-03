//
//  LevelManager.h
//  oneonone
//
//  Created by johan ten broeke on 3/2/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "OOOLevelManager.h"
#import "OOOStore.h"


@interface OOOLevelManager : NSObject {
	NSDictionary *data;
	int progressionIndex;
	int currentLevelIndex;
	int currentTutorialIndex;
	int currentSurvivalIndex;
	NSMutableDictionary *gameprogress;
	int numswipes_used;
	int previousScore;
	int previousSwipes;
	int previousTime;
	//NSMutableDictionary *sheetsInMemory;
	NSDate *start_time;
	int MAX_TIME_POINTS;
	int MAX_SWIPE_POINTS;
	OOOStore *store;
	BOOL highscore;
	int mode;
	
	int survival_score;
	int survival_swipes;
	int survival_level;
	
	int daily_score;
	int daily_swipes;
	
	NSDictionary *achievements;
	int suspence_sound_trigger_swipecounter;
	
	NSString *daynum;
	NSString *datafile_name;
	NSString *leaderboard_id;
	
	BOOL hasTutorials;
}
+(OOOLevelManager *)sharedLevelManager;
-(void) commitScore;
-(void) clearScore;
-(NSString *) currentLevelID;
-(NSArray *) getLevels;
-(void) save;
-(void) unlockNextLevel;
-(void) setCurrentLevelIndex: (int)clid;
-(int) getLevelProgressionIndex;
-(void) addSwipe;
-(void) reportGameCenterScore:(int)_score;
- (void) reportAchievementIdentifier: (NSString*) identifier;
-(NSString *) getResultsForPrevLevel;
-(NSNumber *) getNumStarsForPrevLevel;
-(NSNumber *)getNumSwipesForPrevLevel;
-(int) getStarsForScore: (int)score;
-(void) unlockNextTutorial;
-(void) enterGameMode;
-(void) enterTutorialMode;
-(void) enterSurvivalMode;
-(BOOL) incrementLevel;
-(NSNumber *) getTimeForPrevLevel;
-(BOOL)hasUpgraded;

-(int)getCurrentLevelIndex;
-(BOOL)scoreIsHighScore;

-(void)progressSurvival;
-(BOOL)isSurvival;
-(BOOL)isRandom;
-(void) enterRandomMode;
-(void)calcSurvivalScore;
-(NSDictionary *)getSurvivalScore;
-(void)explicitUpgrade;

-(NSString *)getTotalScore;
-(BOOL)isTutorial;
-(NSString*)getCurrentLevelTitle;
-(void)enterDailyMode;
-(BOOL)isDaily;
-(NSDictionary *)getDailyScore;
-(NSDictionary *)getRandomScore;
-(void) setDayNumber: (NSString *)_num;
-(void) switchContextLevelPack1;
-(void) switchContextLevelPack2;
-(void) switchContextLevelPack3;
-(void) switchContextLevelPack4;
-(void) initialize;
-(BOOL) hasTutorial;

@end
