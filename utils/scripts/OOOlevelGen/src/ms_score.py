import math
# int swipe_value = MAX_SWIPE_POINTS - (MAX_SWIPE_POINTS / par) * numswipes_used;
# int time_value = MAX_TIME_POINTS - (MAX_TIME_POINTS / time_bonus_limit) * sec;

# > 15000 ***
# > 8000 **
# < 8000 *

MAX_TIME_POINTS = 10000
MAX_SWIPE_POINTS = 10000

def calc3StarScoreForSwipes(swipes,secs):
    secs = float(secs)
    for i in (7500,):

        lostpoints = 10000 - i
        a = (lostpoints / swipes)
        par = (10000 / a)

        print "_"*20
        #print "target :",i
        print "swipes : ",swipes," secs : ",secs

        needed_timepoints_for_3_stars = 15000-(MAX_SWIPE_POINTS - (MAX_SWIPE_POINTS / par) * swipes)
        b = (MAX_TIME_POINTS - needed_timepoints_for_3_stars) / secs
        time_bonus_limit = MAX_TIME_POINTS/b

        print "swipes par: ",par
        print "seconds par: ",math.ceil(time_bonus_limit)
        print ""
        print ""
        return (par,int(math.ceil(time_bonus_limit)))

if __name__ == "__main__":
	calc3StarScoreForSwipes(1,1)
