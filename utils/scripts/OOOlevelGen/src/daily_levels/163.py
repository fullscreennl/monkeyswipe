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
	lb.addObject(Hero.HeroSprite(x=22,y=16, friction=2.2))
	#revJoint = Joints.RevoluteJoint(body1='Hero',body2='Balkje',motor_speed='50.0',torque='10000.0',enable_motor='true',lower_angle='12',upper_angle='45',enable_limit='false',collide_connected='false')
	#lb.addObject(revJoint)
	
	
	lb.addObject(Beam.BeamSprite(x=63,y=7,width=126,height=15,static='false',angle=0, friction=2, density=4))
	lb.addObject(Beam.BeamSprite(x=417,y=7,width=126,height=15,static='false',angle=0, friction=2, density=4))

	lb.addObject(Beam.BeamSprite(x=159, y=320-258,width=126,height=15,static='false',angle='67', friction=2, density=4))
	lb.addObject(Beam.BeamSprite(x=321, y=320-258,width=126,height=15,static='false',angle='-67', friction=2, density=4))
	lb.addObject(Beam.BeamSprite(x=240, y=320-190,width=126,height=15,static='false',angle=0, friction=2, density=4))
	
	lb.addObject(Beam.BeamSprite(x=212, y=320-121,width=126,height=15,static='false',angle='67', friction=2, density=4))
	lb.addObject(Beam.BeamSprite(x=272, y=320-121,width=126,height=15,static='false',angle='-67', friction=2, density=4))
	
	lb.addObject(Enemy.EnemySprite(x=240,y=320-32,width=60,height=60, density=1))
	
	for i in range(5):
		if i == 2:
			lb.addObject(Star.StarSprite(x=170 +i*35,y=16,width=32,height=32))
		else:
			lb.addObject(Enemy.EnemySprite(x=170 +i*35,y=16,width=32,height=32, density=5, friction=4))
	for i in range(4):
		lb.addObject(Enemy.EnemySprite(x=189 +i*35,y=320-274,width=32,height=32, density=1, friction=4))
	for i in range(3):
		lb.addObject(Enemy.EnemySprite(x=205 +i*35,y=320- 246,width=32,height=32, density=1, friction=4))
	for i in range(2):
		lb.addObject(Enemy.EnemySprite(x=220 +i*35,y=320-216,width=32,height=32, density=1, friction=4))
		
	#lb.addObject(Beam.BeamSprite(x=128,y=32,width=90,height=15,static='false',angle=45, density=1))
	#lb.addObject(Beam.BeamSprite(x=480-128,y=32,width=90,height=20,static='true',angle=-45, density=1))
	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=320-164,width=38,height=38))
	lb.render()
