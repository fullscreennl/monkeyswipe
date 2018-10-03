import LevelBuilder
from sprites import *

"""
### Creating builder ###

level:    lb = LevelBuilder.LevelBuilder("level_21.plist")

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
	lb.addObject(Hero.HeroSprite(x=80,y=30))
	lb.addObject(Star.StarSprite(x=280,y=305,width=32,height=32,density=1))
	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=100,y=30,width=50,height=50))
	lb.addObject(Rotor.RotorSprite(x=240,y=90,speed=50,torque=10000))
	lb.addObject(Nut.NutSprite(x=240,y=180))
	lb.addObject(Nut.NutSprite(x=160,y=180))
	lb.addObject(Nut.NutSprite(x=320,y=180))
	 
	lb.addObject(Beam.BeamSprite(x=85,y=250,width=170,height=10,static='true',angle=-30))
	lb.addObject(Beam.BeamSprite(x=395,y=250,width=170,height=10,static='true',angle=30))
	lb.addObject(Beam.BeamSprite(x=200,y=190,width=90,height=15,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=280,y=190,width=90,height=15,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=240,y=3,width=480,height=50,static='true',angle=0)) #groundblock
	
	enemies = [(240,300,30),(240,300,30),(440,300,30),(440,300,30),(240,300,30),(240,300,30),(240,300,30),(30,300,30),(30,300,30),(30,300,30),
	(30,300,30),(30,300,30),(30,300,30),(30,300,30),(400,300,30),(400,300,30),(240,300,30),(240,300,30),(240,300,30)]
	#lb.addObject(Enemy.EnemySprite(x=240,y=200,width=320,height=320))
	for enemy in enemies:
		lb.addObject(Enemy.EnemySprite(x=enemy[0], y=enemy[1], width=enemy[2], height=enemy[2]))

	lb.addObject(Enemy.EnemySprite(x=400, y=50, width=32, height=32))
	
	lb.render()
