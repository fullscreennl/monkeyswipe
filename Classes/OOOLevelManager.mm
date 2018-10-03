//
//  LevelManager.m
//  oneonone
//
//  Created by johan ten broeke on 3/2/10.
//  Copyright 2010 fullscreen. All rights reserved.
//

#define Swipe_Master_Bronze @"278144"
#define Swipe_Master_Silver @"298922"
#define Swipe_Master_Gold @"298932" 
#define Enemy_Cruncher_Bronze @"297702" 
#define Enemy_Cruncher_Silver @"298942"
#define Enemy_Cruncher_Gold @"298952"
#define Puzzle_Solver_Bronze @"298962"
#define Puzzle_Solver_Silver @"298972"
#define Puzzle_Solver_Gold @"298982"
#define Monkey_Swipe_King @"299012"

#define Swipe_Master_Bronze_dl @"423944"
#define Swipe_Master_Silver_dl @"424184"
#define Swipe_Master_Gold_dl @"424194" 
#define Enemy_Cruncher_Bronze_dl @"424204" 
#define Enemy_Cruncher_Silver_dl @"424214"
#define Enemy_Cruncher_Gold_dl @"424224"
#define Puzzle_Solver_Bronze_dl @"424234"
#define Puzzle_Solver_Silver_dl @"424254"
#define Puzzle_Solver_Gold_dl @"424474"
#define Monkey_Swipe_King_dl @"424604"


enum {
	kTutorialMode = 1,
	kGameMode = 2,
	kSurvivalMode= 3,
	kDailyMode = 4,
	kRandomMode = 5
};

#import "OOOLevelManager.h"
#import "cocos2d.h"
//#import "OFHighScoreService.h"
//#import "OFAchievementService.h"
//#import "OFAchievement.h"
#import "OOOStore.h"
#import "MainSplash.h"
//#import "OFSocialNotificationService.h"
#import "SimpleAudioEngine.h"
#import <GameKit/GameKit.h>

@implementation OOOLevelManager

static OOOLevelManager *_sharedLevelManager = nil;

+ (OOOLevelManager *)sharedLevelManager
{
	if (!_sharedLevelManager) {
		_sharedLevelManager = [[self alloc] init];
	}
	return _sharedLevelManager;
}

+(id)alloc
{
	NSAssert(_sharedLevelManager == nil, @"Attempted to allocate a second instance of a singleton.");
	return [super alloc];
}

-(id) init
{
	if( (self=[super init])) {
		datafile_name = @"gameprogress";
		leaderboard_id = @"262763";
		achievements = [[NSDictionary dictionaryWithObjectsAndKeys:  Swipe_Master_Bronze,[NSNumber numberWithInt:1],
						 Swipe_Master_Silver,[NSNumber numberWithInt:10],
						 Swipe_Master_Gold,[NSNumber numberWithInt:25],
						 Enemy_Cruncher_Bronze,[NSNumber numberWithInt:12],
						 Enemy_Cruncher_Silver,[NSNumber numberWithInt:27],
						 Enemy_Cruncher_Gold,[NSNumber numberWithInt:38],
						 Puzzle_Solver_Bronze,[NSNumber numberWithInt:7],
						 Puzzle_Solver_Silver,[NSNumber numberWithInt:15],
						 Puzzle_Solver_Gold,[NSNumber numberWithInt:37],
						 Monkey_Swipe_King,[NSNumber numberWithInt:39], nil] retain];
		[self initialize];
	}	
	return self;
}

-(void) initialize{
	NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
	NSString *documentsDirectory = [paths objectAtIndex:0];
	NSString *file = [documentsDirectory stringByAppendingPathComponent:[datafile_name stringByAppendingString:@".plist"]];
	
	gameprogress = [[NSMutableDictionary dictionaryWithContentsOfFile:file] retain];
	
	if(gameprogress == nil){
		NSString *file = [[NSBundle mainBundle] pathForResource:datafile_name ofType:@"plist"];
		gameprogress = [[NSMutableDictionary dictionaryWithContentsOfFile:file]retain];
		//NSLog(@"reading default startup gameprgress file");
	}
	
	progressionIndex = [[gameprogress objectForKey:@"currentlevel"] intValue];
	
	numswipes_used = 0;
	previousScore = 0;
	mode = kTutorialMode;
	currentTutorialIndex = 0;
	currentLevelIndex = 0;
	currentSurvivalIndex = 1;
	
	MAX_TIME_POINTS = 10000;
	MAX_SWIPE_POINTS = 10000;
	
	start_time = [[NSDate date] retain];

	store = [[OOOStore alloc] init];

	suspence_sound_trigger_swipecounter = 0;
	daynum = @"";
	
}

-(void) switchContextLevelPack1{
	//save previous context
	[self save];
	//releas all for re-init
	[datafile_name release];
	[store release];
	[start_time release];
	[achievements release];
	[gameprogress release];
	[daynum release];
	// set new Context
	datafile_name = @"gameprogress";
	leaderboard_id = @"262763";
	hasTutorials = YES;
	achievements = [[NSDictionary dictionaryWithObjectsAndKeys:  Swipe_Master_Bronze,[NSNumber numberWithInt:1],
					 Swipe_Master_Silver,[NSNumber numberWithInt:10],
					 Swipe_Master_Gold,[NSNumber numberWithInt:25],
					 Enemy_Cruncher_Bronze,[NSNumber numberWithInt:12],
					 Enemy_Cruncher_Silver,[NSNumber numberWithInt:27],
					 Enemy_Cruncher_Gold,[NSNumber numberWithInt:38],
					 Puzzle_Solver_Bronze,[NSNumber numberWithInt:7],
					 Puzzle_Solver_Silver,[NSNumber numberWithInt:15],
					 Puzzle_Solver_Gold,[NSNumber numberWithInt:37],
					 Monkey_Swipe_King,[NSNumber numberWithInt:39], nil] retain];
	[self initialize];
}

-(void) switchContextLevelPack2{
	//save previous context
	[self save];
	//releas all for re-init
	[datafile_name release];
	[store release];
	[start_time release];
	[achievements release];
	[gameprogress release];
	[daynum release];
	// set new Context
	datafile_name = @"gameprogress_2";
	leaderboard_id = @"384293";
	hasTutorials = YES;
	achievements = [[NSDictionary dictionaryWithObjectsAndKeys:  Swipe_Master_Bronze,[NSNumber numberWithInt:1],
					 Swipe_Master_Silver,[NSNumber numberWithInt:10],
					 Swipe_Master_Gold,[NSNumber numberWithInt:25],
					 Enemy_Cruncher_Bronze,[NSNumber numberWithInt:12],
					 Enemy_Cruncher_Silver,[NSNumber numberWithInt:27],
					 Enemy_Cruncher_Gold,[NSNumber numberWithInt:38],
					 Puzzle_Solver_Bronze,[NSNumber numberWithInt:7],
					 Puzzle_Solver_Silver,[NSNumber numberWithInt:15],
					 Puzzle_Solver_Gold,[NSNumber numberWithInt:37],
					 Monkey_Swipe_King,[NSNumber numberWithInt:39], nil] retain];
	[self initialize];
}

-(void) switchContextLevelPack3{
	//save previous context
	[self save];
	//releas all for re-init
	[datafile_name release];
	[store release];
	[start_time release];
	[achievements release];
	[gameprogress release];
	[daynum release];
	// set new Context
	datafile_name = @"gameprogress_3";
	leaderboard_id = @"384303";
	hasTutorials = NO;
	achievements = [[NSDictionary dictionaryWithObjectsAndKeys:  Swipe_Master_Bronze_dl,[NSNumber numberWithInt:1],
					 Swipe_Master_Silver_dl,[NSNumber numberWithInt:10],
					 Swipe_Master_Gold_dl,[NSNumber numberWithInt:25],
					 Enemy_Cruncher_Bronze_dl,[NSNumber numberWithInt:12],
					 Enemy_Cruncher_Silver_dl,[NSNumber numberWithInt:27],
					 Enemy_Cruncher_Gold_dl,[NSNumber numberWithInt:38],
					 Puzzle_Solver_Bronze_dl,[NSNumber numberWithInt:7],
					 Puzzle_Solver_Silver_dl,[NSNumber numberWithInt:15],
					 Puzzle_Solver_Gold_dl,[NSNumber numberWithInt:37],
					 Monkey_Swipe_King_dl,[NSNumber numberWithInt:39], nil] retain];
	[self initialize];
}

-(void) switchContextLevelPack4{
	//save previous context
	[self save];
	//releas all for re-init
	[datafile_name release];
	[store release];
	[start_time release];
	[achievements release];
	[gameprogress release];
	[daynum release];
	// set new Context
	datafile_name = @"gameprogress_4";
	leaderboard_id = @"384323";
	hasTutorials = NO;
	achievements = [[NSDictionary dictionaryWithObjectsAndKeys:  Swipe_Master_Bronze_dl,[NSNumber numberWithInt:1],
					 Swipe_Master_Silver_dl,[NSNumber numberWithInt:10],
					 Swipe_Master_Gold_dl,[NSNumber numberWithInt:25],
					 Enemy_Cruncher_Bronze_dl,[NSNumber numberWithInt:12],
					 Enemy_Cruncher_Silver_dl,[NSNumber numberWithInt:27],
					 Enemy_Cruncher_Gold_dl,[NSNumber numberWithInt:38],
					 Puzzle_Solver_Bronze_dl,[NSNumber numberWithInt:7],
					 Puzzle_Solver_Silver_dl,[NSNumber numberWithInt:15],
					 Puzzle_Solver_Gold_dl,[NSNumber numberWithInt:37],
					 Monkey_Swipe_King_dl,[NSNumber numberWithInt:39], nil] retain];
	[self initialize];
}

-(BOOL) hasTutorial{
	return hasTutorials;
}

-(BOOL)hasUpgraded{
	return [store hasUpgraded];
}

-(void)onUpgrade:(NSNotification *) note{
	//NSLog(@"upgrade succes %@",[note name]);
	//NSLog(@"store has upgraded : %i",[store hasUpgraded]);
	[self unlockNextLevel];
	[self incrementLevel];
	
	[[NSNotificationCenter defaultCenter] 
	 postNotification:[NSNotification 
					   notificationWithName:@"reloadLevel" 
					   object:nil 
					   userInfo:nil]];
	
}

-(void)onUpgradeFailed:(NSNotification *) note{
	//NSLog(@"upgrade failed %@ , %@ self %@",[note name],[note object],self);
}

-(void)unlockNextLevel{
	
	//NSLog(@"unlockNextLevel currentLevelIndex %i",currentLevelIndex);
	//NSLog(@"unlockNextLevel progressionIndex %i",progressionIndex);
	//NSLog(@"- - - - - - - - - -");
	
	if (currentLevelIndex == progressionIndex){
		if (progressionIndex >= 9 and [store hasUpgraded] == NO){
			//NSLog(@"YOU MUST UPGRADE TO UNLOCK MORE LEVELS!");
			//[store upgrade];
		}else{
			progressionIndex ++;
			if([achievements objectForKey:[NSNumber numberWithInt:progressionIndex]]){
				//[OFAchievementService unlockAchievement:[achievements objectForKey:[NSNumber numberWithInt:progressionIndex]]];
				//TODO GAMECENTER achievement
                [self reportAchievementIdentifier:[achievements objectForKey:[NSNumber numberWithInt:progressionIndex]]];
               // [[OFAchievement achievement: [achievements objectForKey:[NSNumber numberWithInt:progressionIndex]]] updateProgressionComplete: 100.0f andShowNotification: YES];
			}
			[gameprogress setObject:[NSNumber numberWithInt:progressionIndex] forKey: @"currentlevel"];
		}
	}
	//currentLevelIndex ++;
}


-(void) reportGameCenterScore:(int)_score{
    GKScore *score = nil;
    if (mode == kSurvivalMode){
        score = [[GKScore alloc] initWithCategory:@"287044"];
    }else{
        score = [[GKScore alloc] initWithCategory:leaderboard_id];
    }
    score.value = _score;
    [score reportScoreWithCompletionHandler:^(NSError* error){
        NSLog(@"score submitted ");
        if(error!=nil){
            NSLog(@"Error: %@",[error localizedDescription]);
        }
    }];
}

- (void) reportAchievementIdentifier: (NSString*) identifier
{
    
    if(![MainSplash isGameCenterAPIAvailable]){
        return;
    };
    
    GKAchievement *achievement = [[[GKAchievement alloc] initWithIdentifier: identifier] autorelease];
    if (achievement)
    {
        achievement.percentComplete = 100.0f;
        achievement.showsCompletionBanner = YES;
        [achievement reportAchievementWithCompletionHandler:^(NSError *error)
         {
             if (error == nil)
             {
                 NSLog(@"achievement obtained!!!");
                 // Retain the achievement object and try again later (not shown).
                 //[[OOOLevelManaer get] setGameCenterSubmittedAchivementForID:identifier];
             }else{
                 //NSLog(@"achievement report failed!");
             }
         }];
    }
}


-(NSString*)getCurrentLevelTitle
{
	if (mode == kDailyMode) {
		return @"The daily Swipe.";
	}
	
	NSArray *levels = [gameprogress objectForKey:@"levels"];
	NSMutableDictionary *preview;
	
	if (mode == kSurvivalMode) {
		preview = [levels objectAtIndex:currentSurvivalIndex];
	}else{
		preview = [levels objectAtIndex:currentLevelIndex];
	}
	
	NSString *title = [preview objectForKey:@"levelTitle"];
	return title;
}

-(BOOL)incrementLevel{
	//NSLog(@"incrementLevel currentLevelIndex %i",currentLevelIndex);
	//NSLog(@"incrementLevel progressionIndex %i",progressionIndex);
	//NSLog(@"- - - - - - - - - -");
	if(currentLevelIndex < progressionIndex){
		currentLevelIndex ++;
		return YES;
	}else{
		if ([store hasUpgraded] == NO) {
			[[NSNotificationCenter defaultCenter] removeObserver:self];
			//NSLog(@"YOU MUST UPGRADE TO UNLOCK MORE LEVELS!");
			[[NSNotificationCenter defaultCenter] addObserver:self 
													 selector:@selector(onUpgrade:) 
														 name:@"upgradeSuccess" 
													   object:nil];
			
			[[NSNotificationCenter defaultCenter] addObserver:self 
													 selector:@selector(onUpgradeFailed:) 
														 name:@"upgradeFailed" 
													   object:nil];
			[store upgrade];
		}
		return NO;
	}
}

-(void)explicitUpgrade{
	[[NSNotificationCenter defaultCenter] removeObserver:self];
	[store upgrade];
}

-(void)enterDailyMode{
	mode = kDailyMode;
	daily_score = 0;
	daily_swipes = 0;
}

-(void)enterGameMode{
	mode = kGameMode;
}

-(void)enterTutorialMode{
	mode = kTutorialMode;
}


-(float)getRandomNr{
	//returns random value between 0 and 1 in thousand steps
	uint r = arc4random();
	float rnd  = (r % 1000)/1000.0;
	return rnd;
}

-(void)enterRandomMode{
	
	int random1 = round([self getRandomNr]*3.0);
	//NSLog(@"random1: %i",random1);
	if (random1==0){
		[self switchContextLevelPack1];
	}else if (random1==1){
		[self switchContextLevelPack2];
	}else if (random1==2){
		[self switchContextLevelPack3];
	}else if (random1==3){
		[self switchContextLevelPack4];
	}
	mode = kRandomMode;
	int random2 = round([self getRandomNr]*38.0)+1;
	//NSLog(@"random2: %i",random2);
	[self setCurrentLevelIndex:random2];
}



-(void)enterSurvivalMode{
	[self switchContextLevelPack2];
	survival_swipes = 0;
	currentSurvivalIndex = 1;
	mode = kSurvivalMode;
}

-(BOOL)isDaily{
	if (mode == kDailyMode){
		return YES;
	}else{
		return NO;
	}
}

-(BOOL)isRandom{
	if (mode == kRandomMode){
		return YES;
	}else{
		return NO;
	}
}

-(BOOL)isSurvival{
	if (mode == kSurvivalMode){
		return YES;
	}else{
		return NO;
	}
}

-(BOOL)isTutorial{
	if (mode == kTutorialMode){
		return YES;
	}else{
		return NO;
	}
}

-(void) addSwipe{
	if (numswipes_used == 0){
		[start_time release];
		start_time = [[NSDate date] retain];
		//NSLog(@"start time %@",start_time);
	}
	if (suspence_sound_trigger_swipecounter%5 == 0 and suspence_sound_trigger_swipecounter!= 0) {
		[[SimpleAudioEngine sharedEngine] playEffect:@"suspence_1.mp3"];
	}
	if (suspence_sound_trigger_swipecounter%13 == 0) {
		[[SimpleAudioEngine sharedEngine] playEffect:@"suspence_2.mp3"];
	}
	suspence_sound_trigger_swipecounter ++;
	numswipes_used ++;
	//NSLog(@"num swipes: %i",suspence_sound_trigger_swipecounter);
}

-(int)calcTotalScore{
	int total_score = 0;
	NSArray *all_levels = [gameprogress objectForKey:@"levels"];
	for (uint i=0; i < [all_levels count]; i++) {
		int level_score = [[[all_levels objectAtIndex:i] objectForKey:@"score"] intValue];
		//NSLog(@"level_score : %i",level_score);
		total_score += level_score;
	}
	//NSLog(@"- - - - - - - ");
	//NSLog(@"total_score : %i",total_score);
	return total_score;
}

-(void)progressSurvival{
	[self calcSurvivalScore];
	currentSurvivalIndex ++;
}

-(void)calcSurvivalScore{
	//NSLog(@" num swipes: %i",numswipes_used);
	survival_swipes += numswipes_used;
	survival_level = currentSurvivalIndex;
	int swipe_score = 10000 - (numswipes_used * 250);
	if (swipe_score < 0){
		swipe_score = 0;
	}
	survival_score += (10000 + swipe_score);
	numswipes_used = 0;
}

-(NSDictionary *) getSurvivalScore{
	int currenrtSurvivalHighScore  = [[gameprogress objectForKey:@"survival_highscore"] intValue];
	int isHighScore = 0;
    NSLog(@"survival score: %i, oldhighscore: %i",survival_score ,currenrtSurvivalHighScore);
	if((currenrtSurvivalHighScore < survival_score) ){
		isHighScore = 1;
        NSLog(@"trying to submit survival score!!!");
		[gameprogress setObject:[NSNumber numberWithInt:survival_score] forKey:@"survival_highscore"];
		//[OFHighScoreService setHighScore:survival_score forLeaderboard:@"287044" onSuccess:OFDelegate() onFailure:OFDelegate()];
        //leaderboard_id = @"287044";
        [self reportGameCenterScore:survival_score];
		//NSString *str = [NSString stringWithFormat:@"just got a new Highscore (%@) in MonkeySwipe survival mode! (reached level %@).",[[NSNumber numberWithInt:survival_score] stringValue],[[NSNumber numberWithInt:survival_level+1] stringValue]];
        //TODO GAMECENTER submit survival score
		//[OFSocialNotificationService sendWithText:str imageNamed:@"notify_monkey_swipe"];
		[self save];
	}
	NSDictionary *survival_result = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithInt:survival_swipes],@"swipes",
																				[NSNumber numberWithInt:survival_score],@"score",
																				[NSNumber numberWithInt:survival_level+1],@"level",
																				[NSNumber numberWithInt:isHighScore],@"highscore",nil];
	//NSLog(@"survival result : %@",survival_result);
	survival_swipes = 0;
	currentSurvivalIndex = 1;
	survival_level = 0;
	survival_score = 0;
	numswipes_used = 0;
	return survival_result;
}

-(void) setDayNumber: (NSString *)_num{
	daynum = _num;
	[daynum retain];
}

-(NSDictionary *)getDailyScore{
	daily_swipes = numswipes_used;
	
	NSDate *end_time = [NSDate date];
	int sec = round([end_time timeIntervalSinceDate:start_time]);
	
	int swipe_value = MAX_SWIPE_POINTS - (MAX_SWIPE_POINTS / 75) * numswipes_used;
	int time_value = MAX_TIME_POINTS - (MAX_TIME_POINTS / 300) * sec;
	
	daily_score = swipe_value + time_value;
	if (daily_score < 0){
		daily_score = 0;
	}
	
	NSString *str = [NSString stringWithFormat:@"I Played the free Daily Swipe No.(%@) and scored (%@) points in MonkeySwipe!",daynum,[[NSNumber numberWithInt:daily_score] stringValue]];
	//[OFSocialNotificationService sendWithText:str imageNamed:@"notify_monkey_swipe"];
	NSDictionary *daily_result = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithInt:daily_swipes],@"swipes",
																			[NSNumber numberWithInt:daily_score],@"score",nil];
	
	numswipes_used = 0;
	return daily_result;
}


-(NSDictionary *)getRandomScore{
	daily_swipes = numswipes_used;
	
	NSDictionary *currLevel  = [[gameprogress objectForKey:@"levels"] objectAtIndex:currentLevelIndex]; 
	
	int par = [[currLevel objectForKey:@"par"]intValue];
	int time_bonus_limit = [[currLevel objectForKey:@"tbl"]intValue];
	
	
	
	NSDate *end_time = [NSDate date];
	int sec = round([end_time timeIntervalSinceDate:start_time]);
	
	int swipe_value = MAX_SWIPE_POINTS - (MAX_SWIPE_POINTS / par) * numswipes_used;
	int time_value = MAX_TIME_POINTS - (MAX_TIME_POINTS / time_bonus_limit) * sec;
	
	daily_score = swipe_value + time_value;
	if (daily_score < 0){
		daily_score = 0;
	}
	int numStars = [self getStarsForScore:daily_score];
	//NSString *str = [NSString stringWithFormat:@"I Played the free Daily Swipe No.(%@) and scored (%@) points in MonkeySwipe!",daynum,[[NSNumber numberWithInt:daily_score] stringValue]];
	//[OFSocialNotificationService sendWithText:str imageNamed:@"notify_monkey_swipe"];
	NSDictionary *daily_result = [NSDictionary dictionaryWithObjectsAndKeys:[NSNumber numberWithInt:daily_swipes],@"swipes",
								  [NSNumber numberWithInt:daily_score],@"score", [NSNumber numberWithInt:sec],@"seconds", [NSNumber numberWithInt:numStars],@"stars",nil];
	
	numswipes_used = 0;
	return daily_result;
}

-(int)calcScore{
	
	NSDictionary *currLevel  = [[gameprogress objectForKey:@"levels"] objectAtIndex:currentLevelIndex]; 
	
	int par = [[currLevel objectForKey:@"par"]intValue];
	int time_bonus_limit = [[currLevel objectForKey:@"tbl"]intValue];
	
	
	
	NSDate *end_time = [NSDate date];
	int sec = round([end_time timeIntervalSinceDate:start_time]);
	
	int swipe_value = MAX_SWIPE_POINTS - (MAX_SWIPE_POINTS / par) * numswipes_used;
	int time_value = MAX_TIME_POINTS - (MAX_TIME_POINTS / time_bonus_limit) * sec;
	
	/**
	NSLog(@"num swipes used %i",numswipes_used);
	NSLog(@"num secs used %i",sec);
	
	NSLog(@"swipes val %i",swipe_value);
	NSLog(@"time val %i",time_value);
	*/
	
	int score = swipe_value + time_value;
	if (score < 0){
		score = 0;
	}
	previousScore = score;
	previousTime = sec;
	
	return score;
}

-(void) commitScore{
	int oldScore = [[[[gameprogress objectForKey:@"levels"] objectAtIndex:currentLevelIndex] objectForKey:@"score"]intValue];
	int score = [self calcScore];
	if (score > oldScore) {
		[[[gameprogress objectForKey:@"levels"] objectAtIndex:currentLevelIndex] setObject:[NSNumber numberWithInt:score] forKey:@"score"];
		//TODO commit gamecenter score
         [self reportGameCenterScore:[self calcTotalScore]];
        //[OFHighScoreService setHighScore:[self calcTotalScore] forLeaderboard:leaderboard_id onSuccess:OFDelegate() onFailure:OFDelegate()];
		//NSLog(@"Oldscore: %i Committing score: %i -> for levelindex: %i",oldScore,score, currentLevelIndex);
		highscore = YES;
	}else{
		//NSLog(@"Oldscore: %i NOT Comitting score: %i -> for levelindex: %i",oldScore,score, currentLevelIndex);
		highscore = NO;
	}
	previousSwipes = numswipes_used;
	numswipes_used = 0;
}

-(void) clearScore{
	numswipes_used = 0;
}

-(NSArray *)getLevels{
	return [gameprogress objectForKey:@"levels"];
}

-(int) getLevelProgressionIndex{
	return progressionIndex;
}

-(void) setCurrentLevelIndex: (int)clid{
	currentLevelIndex = clid;
}

-(int)getStarsForScore: (int)score{
	if (score < 8000) {
		return 1;
	}else if (score > 14999) {
		return 3;
	}else{
		return 2;
	}
}

-(NSString *)getResultsForPrevLevel{
	int oldScore = previousScore;
	NSNumber *score = [NSNumber numberWithInt:oldScore];
	return [NSString stringWithString:[score stringValue]];
}

-(NSString *)getTotalScore{
	NSNumber *score = [NSNumber numberWithInt:[self calcTotalScore]];
	return [NSString stringWithString:[score stringValue]];
}

-(BOOL)scoreIsHighScore{
	return highscore;
}

-(NSNumber *)getNumStarsForPrevLevel{
	int oldScore = previousScore;
	int numStars = [self getStarsForScore:oldScore];
	return [NSNumber numberWithInt:numStars];	
}

-(NSNumber *)getTimeForPrevLevel{
	return [NSNumber numberWithInt:previousTime];	
}

-(NSNumber *)getNumSwipesForPrevLevel{
	return [NSNumber numberWithInt:previousSwipes];	
}

-(void)unlockNextTutorial{
	currentTutorialIndex ++;
}

-(int)getCurrentLevelIndex{
	return currentLevelIndex;
}

-(NSString *)currentLevelID{
	if (mode == kTutorialMode){
		return [[[gameprogress objectForKey:@"tutorials"] objectAtIndex:currentTutorialIndex] objectForKey:@"id"];
	}else if(mode == kSurvivalMode){
		return [[[gameprogress objectForKey:@"levels"] objectAtIndex:currentSurvivalIndex] objectForKey:@"id"];
	}else{
		return [[[gameprogress objectForKey:@"levels"] objectAtIndex:currentLevelIndex] objectForKey:@"id"];
	}
}

-(void)save{
	NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
	NSString *documentsDirectory = [paths objectAtIndex:0];
	NSString *file = [documentsDirectory stringByAppendingPathComponent:[datafile_name stringByAppendingString:@".plist"]];
	//NSLog(@"saving data %@", file);
	[gameprogress writeToFile:file atomically:YES];
}

-(void)dealloc{
	[datafile_name release];
	[store release];
	[start_time release];
	[achievements release];
	[gameprogress release];
	[daynum release];
	[super dealloc];
}
@end
