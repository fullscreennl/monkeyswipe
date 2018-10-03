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
	lb.addObject(Hero.HeroSprite(x=42, y=303,width=32,height=32))	lb.addObject(Beam.BeamSprite(x=420, y=202,width=127,height=14,static='true',angle='0'))	lb.addObject(Enemy.EnemySprite(x=449, y=232,width=52,height=52,static='false',angle='0'))	lb.addObject(Beam.BeamSprite(x=179, y=266,width=368,height=14,static='true',angle='-6'))	lb.addObject(Beam.BeamSprite(x=65, y=110,width=127,height=14,static='true',angle='0'))	lb.addObject(Enemy.EnemySprite(x=39, y=140,width=52,height=52,static='false',angle='0'))	lb.addObject(Beam.BeamSprite(x=250, y=184,width=224,height=14,static='true',angle='9'))	lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='cyclingobject',x=80,y=213,width=72,height=72,enemy_size=16))	lb.addObject(Beam.BeamSprite(x=238, y=128,width=224,height=14,static='true',angle='9'))	lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=410,y=94,scaling=1,speed=0,torque=10))	lb.addObject(Beam.BeamSprite(x=241, y=21,width=224,height=14,static='true',angle='14'))	lb.addObject(Star.StarSprite(x=47, y=22,width=32,height=32))
	lb.render()
