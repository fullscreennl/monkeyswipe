import LevelBuilder
from sprites import *

"""
### Creating builder ###

level:    lb = LevelBuilder.LevelBuilder("level_34.plist")

### Adding sprites ###

Hero:     lb.addObject(Hero.HeroSprite(x=20,y=10))

Rotor:    lb.addObject(Rotor.RotorSprite(x=180,y=110,speed=5,torque=10000))

Bucket:   lb.addObject(EnemyBucketWithStar.EnemyBucketWithStarSprite(width=100,height=75, x=240, y=160, num_enemies=10, enemy_size=20))

Launcher: lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=260, y=50, trigger_x=400, trigger_y=100))

Beam:     lb.addObject(Beam.BeamSprite(x=240+40,y=25,width=30,height=60,static='true',angle=0))

Nut:      lb.addObject(Nut.NutSprite(x=50,y=200))

Enemy:    lb.addObject(Enemy.EnemySprite(x=240,y=200,width=50,height=50))

Friend:   lb.addObject(Friend.FriendSprite(x=240,y=125,width=128,height=128))

Wizard:   lb.addObject(Wizard.WizardSprite(x=25,y=50))

Spikey:   lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=50,y=80,width=50,height=50))

### Custom names ###

Setting custom Name (for joints and Contact defs): Hero.HeroSprite(x=20,y=10).setName("piet")


### Adding Joints ###

RevJoint:   revJoint = Joints.RevoluteJoint(body1='body_1',body2='body_2',motor_speed='50.0',torque='1000.0',enable_motor='true',lower_angle='12',upper_angle='45',enable_limit='false',collide_connected='false')
            lb.addObject(revJoint)
          
PrismJoint: prismJoint = Joints.PrismaticJoint(body1='body_1',motor_speed='50.0',torque='1000.0',enable_motor='true',lower_translation='-100',upper_translation='100',enable_limit='false',vertical=False)
            lb.addObject(prismJoint)
            
DistJoint:  distJoint = Joints.DistanceJoint(body1='body_1',body2='body_2',damping='0.2',freq='0.8')   
            lb.addObject(distJoint)
            
### Adding Contacts ###

Contact: Contacts.Contact(body1='test',body2='test2',event_name='onTest')
            
lb.render()

"""
def render(name,bg):
	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
	#lb.addObject(Beam.BeamSprite(x=32,y=16,width=35,height=15,static='false',angle=0, density=1).setName("Balkje"))
	lb.addObject(Friend.FriendSprite(x=251, y=152,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=266, y=118,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=213, y=150,width=60,height=60,density=1,angle='15'))	lb.addObject(Friend.FriendSprite(x=346, y=182,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=361, y=153,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=322, y=153,width=38,height=38,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=308, y=185,width=32,height=32,density=1,angle='-30'))	lb.addObject(Friend.FriendSprite(x=286, y=153,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=259, y=222,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=274, y=188,width=40,height=40,density=1,angle='-15'))	lb.addObject(Friend.FriendSprite(x=235, y=188,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=221, y=220,width=32,height=32,density=1,angle='15'))	lb.addObject(Friend.FriendSprite(x=199, y=188,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=160, y=193,width=32,height=32,density=1,angle='15'))	lb.addObject(Friend.FriendSprite(x=175, y=159,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=136, y=159,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=122, y=191,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=100, y=159,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=144, y=127,width=62,height=64,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=185, y=102,width=32,height=32,density=1,angle='-90'))	lb.addObject(Friend.FriendSprite(x=120, y=93,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=106, y=125,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=68, y=121,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=343, y=118,width=32,height=32,density=1,angle='15'))	lb.addObject(Friend.FriendSprite(x=358, y=87,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=305, y=116,width=44,height=44,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=358, y=289,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=453, y=202,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=364, y=222,width=52,height=52,density=1,angle='-30'))	lb.addObject(Friend.FriendSprite(x=140, y=223,width=32,height=32,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=318, y=225,width=32,height=32,density=1,angle='0'))	lb.addObject(Enemy.EnemySprite(x=386, y=180,width=32,height=32,static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=286, y=232,width=32,height=32,static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=181, y=225,width=32,height=32,static='false',angle='0'))	lb.addObject(Friend.FriendSprite(x=237, y=51,width=102,height=102,density=1,angle='-45'))	lb.addObject(Friend.FriendSprite(x=53, y=260,width=102,height=102,density=1,angle='30'))	lb.addObject(Friend.FriendSprite(x=145, y=280,width=76,height=76,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=428, y=60,width=102,height=102,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=428, y=267,width=102,height=102,density=1,angle='15'))	lb.addObject(Friend.FriendSprite(x=51, y=52,width=102,height=102,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=225, y=276,width=76,height=76,density=1,angle='-45'))	lb.addObject(Friend.FriendSprite(x=432, y=147,width=76,height=76,density=1,angle='45'))	lb.addObject(Friend.FriendSprite(x=330, y=39,width=76,height=76,density=1,angle='45'))	lb.addObject(Friend.FriendSprite(x=39, y=169,width=76,height=76,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=142, y=40,width=76,height=76,density=1,angle='0'))	lb.addObject(Friend.FriendSprite(x=301, y=283,width=76,height=76,density=1,angle='0'))	lb.addObject(Star.StarSprite(x=381, y=117,width=32,height=32))	lb.addObject(Hero.HeroSprite(x=88, y=196,width=32,height=32))	lb.render()
