import LevelBuilder
from sprites import *
"""
### Creating builder ###

level:    lb = LevelBuilder.LevelBuilder("level_34.plist")

### Adding sprites ###

Hero:     lb.addObject(Hero.HeroSprite(x=20,y=10))

Rotor:    lb.addObject(Rotor.RotorSprite(x=180,y=110,speed=5,torque=10000))

Bucket:   lb.addObject(EnemyBucketWithStar.EnemyBucketWithStarSprite(width=100,height=75, x=240, y=160, num_enemies=10, enemy_size=20))

Launcher: lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=260, y=50, trigger_x=400, trigger_y=100,power='#20000'))

Beam:     lb.addObject(Beam.BeamSprite(x=240+40,y=25,width=30,height=60,static='true',angle=0))

Nut:      lb.addObject(Nut.NutSprite(x=50,y=200))

Enemy:    lb.addObject(Enemy.EnemySprite(x=240,y=200,width=50,height=50))

Friend:   lb.addObject(Friend.FriendSprite(x=240,y=125,width=128,height=128))

Wizard:   lb.addObject(Wizard.WizardSprite(x=25,y=50))

Spikey:   lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=50,y=80,width=50,height=50))

EnemyEquipedRotor: lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=160,y=240,speed=2,torque=10000))
CyclingEnemyObject : CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=240,y=160,width=120,height=120,enemy_size=40)

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

	lb.addObject(Hero.HeroSprite(x=90,y=200))

	#lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=160,width=32,height=32,density='1',restitution='0.7'))
	
	#static beams
	lb.addObject(Beam.BeamSprite(x=40,y=180,width=80,height=24,static='true',angle=0))
	lb.addObject(Beam.BeamSprite(x=240,y=180,width=264,height=24,static='true',angle=0))
	lb.addObject(Beam.BeamSprite(x=440,y=180,width=80,height=24,static='true',angle=0))
	
	lb.addObject(Beam.BeamSprite(x=240,y=52,width=104,height=25,static='true',angle=90))
	#dynamic beams
	lb.addObject(Beam.BeamSprite(x=25,y=202,width=20,height=20,static='false',angle=0,density=15))
	lb.addObject(Beam.BeamSprite(x=30,y=222,width=20,height=20,static='false',angle=0,density=15))
	lb.addObject(Beam.BeamSprite(x=25,y=242,width=20,height=20,static='false',angle=0,density=15))
	
	lb.addObject(Beam.BeamSprite(x=175,y=202,width=20,height=20,static='false',angle=0,density=15))
	lb.addObject(Beam.BeamSprite(x=180,y=222,width=20,height=20,static='false',angle=0,density=15))
	lb.addObject(Beam.BeamSprite(x=175,y=242,width=20,height=20,static='false',angle=0,density=15))
	
	lb.addObject(Beam.BeamSprite(x=225,y=202,width=20,height=20,static='false',angle=0,density=15))
	lb.addObject(Beam.BeamSprite(x=230,y=222,width=20,height=20,static='false',angle=0,density=15))
	lb.addObject(Beam.BeamSprite(x=225,y=242,width=20,height=20,static='false',angle=0,density=15))
	
	#wipwap dyn part
	lb.addObject(Beam.BeamSprite(x=240, y= 100 ,width=360,height=20,static='false',angle=0))
	offset=8
	lb.addObject(Beam.BeamSprite(x=80-offset, y= 113 ,width=10,height=5,static='false',friction=20,angle=0))
	lb.addObject(Beam.BeamSprite(x=108-offset, y= 113 ,width=20,height=5,static='false',friction=20,angle=0))
	lb.addObject(Star.StarSprite(x=90-offset,y=141,width=26,height=26))
	
	lb.addObject(Beam.BeamSprite(x=400+offset, y= 113 ,width=30,height=20,static='false',friction=20, angle=0,density=20))
	#lb.addObject(Beam.BeamSprite(x=370+offset, y= 113 ,width=20,height=5,static='false',angle=0))
	#lb.addObject(Friend.FriendSprite(x=480-90+offset,y=141,width=26,height=26))
	
	
	lb.addObject(Enemy.EnemySprite(y=270,x=25,width=32,height=32,density='1',static='false'))
	#lb.addObject(Enemy.EnemySprite(y=270,x=175,width=32,height=32,density='1',static='false'))
	#lb.addObject(Enemy.EnemySprite(y=270,x=225,width=32,height=32,density='1',static='false'))
	
	lb.render()
