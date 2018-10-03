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
	lb.addObject(Star.StarSprite(x=440,y=10,width=50,height=50))
	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=460,y=10,width=60,height=60))
	
	lb.addObject(Beam.BeamSprite(x=336,y=128,width=256,height=50,static='true',angle=90))
	
	#firstfloor
	lb.addObject(Beam.BeamSprite(x=48,y=64,width=96,height=20,static='true',angle=0))
	
	lb.addObject(Nut.NutSprite(x=140,y=52))
	lb.addObject(Nut.NutSprite(x=180,y=52))
	lb.addObject(Beam.BeamSprite(x=160,y=64,width=64,height=20,static='false',angle=0))
	
	lb.addObject(Beam.BeamSprite(x=276,y=64,width=96,height=20,static='true',angle=0))
	
	lb.addObject(Enemy.EnemySprite(x=112,y=80,width=52,height=52))
	lb.addObject(Enemy.EnemySprite(x=208,y=80,width=52,height=52))
	
	
	#secondfloor
	lb.addObject(Nut.NutSprite(x=160,y=152))
	lb.addObject(Beam.BeamSprite(x=160,y=160,width=256,height=20,static='false',angle=0))
	lb.addObject(Enemy.EnemySprite(x=64,y=192,width=72,height=72))
	lb.addObject(Enemy.EnemySprite(x=256,y=192,width=72,height=72))
	
	#third floor
	lb.addObject(Nut.NutSprite(x=160,y=224))
	lb.addObject(Enemy.EnemySprite(x=160,y=250,width=72,height=72))
	
	#lb.addObject(Enemy.EnemySprite(x=240,y=200,width=320,height=320))
	
	lb.addObject(Nut.NutSprite(x=416,y=300).setName("keyNut"))
	lb.addObject(Enemy.EnemySprite(x=416,y=192,width=120,height=120).setName("keyEnemy"))
	
	distJoint = Joints.DistanceJoint(body1='keyNut',body2='keyEnemy',damping='0.2',freq='0.8')   
	lb.addObject(distJoint)
	
	lb.addObject(Contacts.Contact(body1='keyNut',body2='Hero',event_name='onNutHit'))
	lb.addObject(Contacts.Contact(body1='keyEnemy',body2='Hero',event_name='onLose'))
	lb.addObject(Contacts.Contact(body1='keyEnemy',body2='Spikey',event_name='onDestroy'))
	lb.render()
