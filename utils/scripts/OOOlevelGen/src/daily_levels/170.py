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
	lb.addObject(Beam.BeamSprite(x=440, y=227,width=91,height=9,static='true',angle='5'))	lb.addObject(Beam.BeamSprite(x=384, y=268,width=95,height=14,static='false',angle='90').setName('beamLatch'))	lb.addObject(Nut.NutSprite(x=366, y=230,width=18,height=18))	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=448, y=256,width=32,height=32, density=1, restitution=0.8))	lb.addObject(Nut.NutSprite(x=384, y=273,width=18,height=18).setName('axis'))	lb.addObject(Joints.RevoluteJoint(body1='axis',body2='beamLatch',motor_speed='-1',enable_motor='true',torque='100',lower_angle='-90',upper_angle='180',enable_limit='true',collide_connected='false'))	lb.addObject(Hero.HeroSprite(x=60, y=16,width=32,height=32))	lb.addObject(Beam.BeamSprite(x=251, y=79,width=159,height=14,static='true',angle='90'))	lb.addObject(Beam.BeamSprite(x=311, y=174,width=127,height=14,static='false',angle='-90').setName('latch2'))	lb.addObject(Nut.NutSprite(x=310, y=173,width=18,height=18).setName('axis2'))	lb.addObject(Joints.RevoluteJoint(body1='axis2',body2='latch2',motor_speed='-1',enable_motor='false',torque='100',lower_angle='-90',upper_angle='180',enable_limit='false',collide_connected='false'))	lb.addObject(Beam.BeamSprite(x=193, y=79,width=159,height=14,static='true',angle='90'))	lb.addObject(Enemy.EnemySprite(x=227, y=148,width=32,height=32,static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=227, y=116,width=32,height=32,static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=227, y=84,width=32,height=32,static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=227, y=51,width=32,height=32,static='false',angle='0'))	lb.addObject(Star.StarSprite(x=228, y=17,width=32,height=32))
	lb.render()
