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
	lb.addObject(Enemy.EnemySprite(x=29, y=106,width=32,height=32,density='1',static='false',angle='0').setName('en4'))	lb.addObject(Hero.HeroSprite(x=76, y=85,width=32,height=32))	lb.addObject(Enemy.EnemySprite(x=121, y=109,width=32,height=32,density='1',static='false',angle='0').setName('en2'))	lb.addObject(Enemy.EnemySprite(x=76, y=36,width=32,height=32,density='150',static='false',angle='0').setName('en0'))	lb.addObject(Enemy.EnemySprite(x=29, y=59,width=32,height=32,density='1',static='false',angle='0').setName('en5'))	lb.addObject(Enemy.EnemySprite(x=121, y=55,width=32,height=32,density='150',static='false',angle='0').setName('en1'))	lb.addObject(Enemy.EnemySprite(x=76, y=133,width=32,height=32,density='1',static='false',angle='0').setName('en3'))	lb.addObject(Joints.DistanceJoint(body1='en0',body2='en1',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en0',body2='en2',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en1',body2='en2',damping='0.2',freq='5'))	lb.addObject(Joints.DistanceJoint(body1='en1',body2='en3',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en2',body2='en3',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en2',body2='en4',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en3',body2='en4',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en3',body2='en5',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en4',body2='en5',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en4',body2='en0',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en5',body2='en0',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en5',body2='en1',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='Hero',body2='en0',damping='0.2',freq='20'))	lb.addObject(Joints.DistanceJoint(body1='en3',body2='Hero',damping='0.2',freq='20'))	lb.addObject(Beam.BeamSprite(x=254, y=0,width=588,height=63,static='true',angle='8'))	lb.addObject(Contacts.Contact(body1='Hero',body2='en0',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='en1',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='en3',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='en2',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='en4',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='en5',event_name='onLose'))	lb.addObject(Nut.NutSprite(x=408, y=306,width=14,height=14))	lb.addObject(Star.StarSprite(x=408, y=89,width=32,height=32))	lb.addObject(Joints.DistanceJoint(body1='Nut',body2='Star',damping='0.2',freq='2'))	lb.render()
