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
	lb = LevelBuilder.LevelBuilder(name+".plist", background=bg)
	
	lb.addObject(Hero.HeroSprite(x=20,y=10))
	
	
	lb.addObject(Beam.BeamSprite(x=48,y=134,width=272,height=20,static='true',angle=90))
	lb.addObject(Beam.BeamSprite(x=106,y=48,width=96,height=20,static='true',angle=90))
	lb.addObject(Beam.BeamSprite(x=106,y=240,width=160,height=20,static='true',angle=90))
	lb.addObject(Beam.BeamSprite(x=106,y=129,width=62,height=20,static='false',angle=90)) #fallout
	lb.addObject(Beam.BeamSprite(x=270,y=175,width=310,height=30,static='true',angle=0))
	lb.addObject(Beam.BeamSprite(x=247,y=130,width=160,height=20,static='true',angle=90))
	lb.addObject(Beam.BeamSprite(x=304,y=48,width=96,height=20,static='true',angle=90))
	lb.addObject(Beam.BeamSprite(x=432,y=160,width=240,height=20,static='true',angle=90))
	
	lb.addObject(Beam.BeamSprite(x=256,y=224,width=270,height=20,static='false',angle=0)) #wipwap
	lb.addObject(Beam.BeamSprite(x=247,y=290,width=60,height=20,static='true',angle=90))
	lb.addObject(Enemy.EnemySprite(x=138,y=250,width=42,height=42))
	lb.addObject(Star.StarSprite(x=148,y=260,width=20,height=20))
	
	
	lb.addObject(Rotor.RotorSprite(x=182,y=80,speed=0,torque=100))
	lb.addObject(Rotor.RotorSprite(x=370,y=80,speed=0,torque=100))
	
	lb.addObject(Enemy.EnemySprite(x=170,y=96,width=22,height=22))
	lb.addObject(Enemy.EnemySprite(x=194,y=96,width=22,height=22))
	
	lb.render()
