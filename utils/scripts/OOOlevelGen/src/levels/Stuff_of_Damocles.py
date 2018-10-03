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

	lb.addObject(Hero.HeroSprite(x=20,y=10))
	lb.addObject(Friend.FriendSprite(x=213,y=320,width=15,height=15,static='true'))
	lb.addObject(Star.StarSprite(x=213,y=300,width=32,height=32))
	
	lb.addObject(Nut.NutSprite(x=15,y=160, eventName='onNutHitAll'))
	lb.addObject(Nut.NutSprite(x=205,y=300, eventName='onNutHitAll'))
	lb.addObject(Nut.NutSprite(x=225,y=300, eventName='onNutHitAll'))
	lb.addObject(Nut.NutSprite(x=460,y=136, eventName='onNutHitAll'))
	lb.addObject(Nut.NutSprite(x=240,y=30, eventName='onNutHitAll'))

	for n in range(15):
		lb.addObject(Nut.NutSprite(x=90 + (n*20),y=180, eventName='onNutHitAll'))
	
	
	
	
	#2 main beams for holding back loads of enemies
	lb.addObject(Beam.BeamSprite(x=104,y=245,width=250,height=20,static='false',angle=35))
	lb.addObject(Beam.BeamSprite(x=350,y=240,width=310,height=20,static='false',angle=-35,density=1))
	
	#several small beams
	#lb.addObject(Beam.BeamSprite(x=50,y=45,width=50,height=20,static='true',angle=0))
	#lb.addObject(Nut.NutSprite(x=50,y=70, eventName='onNutHitAll'))
	
	#lb.addObject(Beam.BeamSprite(x=260,y=110,width=90,height=80,static='true',angle=0))
	#lb.addObject(Nut.NutSprite(x=260,y=140, eventName='onNutHitAll'))
	
	#lb.addObject(Beam.BeamSprite(x=140,y=150,width=190,height=20,static='true',angle=0))
	#lb.addObject(Nut.NutSprite(x=90,y=180, eventName='onNutHitAll'))
	#lb.addObject(Nut.NutSprite(x=170,y=180, eventName='onNutHitAll'))
	
	#lb.addObject(Beam.BeamSprite(x=390,y=45,width=90,height=20,static='true',angle=0))
	#lb.addObject(Nut.NutSprite(x=390,y=70, eventName='onNutHitAll'))
	
	for i in range(15):
		lb.addObject(Enemy.EnemySprite(x=40,y=300,width=32,height=32, density=2))
	
	for i in range(10):
		lb.addObject(Enemy.EnemySprite(x=380,y=290,width=32,height=32, density=2))
	for i in range(13):
		lb.addObject(Enemy.EnemySprite(x=430,y=300,width=32,height=32, density=2))
		
	lb.addObject(Enemy.EnemySprite(x=240-20,y=200,width=32,height=32, density=2))
	lb.addObject(Enemy.EnemySprite(x=240+20,y=200,width=32,height=32, density=2))
	lb.addObject(Enemy.EnemySprite(x=240+80,y=200,width=32,height=32, density=2))
	lb.addObject(Enemy.EnemySprite(x=240-60,y=200,width=32,height=32, density=2))
	lb.addObject(Enemy.EnemySprite(x=240-120,y=200,width=32,height=32, density=2))


	lb.addObject(Enemy.EnemySprite(x=390,y=64,width=128,height=128, density=2))
	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=320,y=20,width=40,height=40,density=6,restitution=0.6))
	
	distJoint = Joints.DistanceJoint(body1='Star',body2='Friend',damping='0.2',freq='0.8')   
	lb.addObject(distJoint)
	            
	lb.render()
