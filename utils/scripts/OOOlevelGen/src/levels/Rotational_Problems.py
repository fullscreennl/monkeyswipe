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
    
    lb.addObject(Star.StarSprite(x=460,y=300,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=450,y=270,width=60,height=20,static='true',angle=0))
    
    lb.addObject(Rotor.RotorSprite(x=60,y=160,speed=5,torque=10000))
    lb.addObject(Rotor.RotorSprite(x=180,y=160,speed=1,torque=10000))
    lb.addObject(Rotor.RotorSprite(x=300,y=160,speed=-5,torque=10000))
    lb.addObject(Rotor.RotorSprite(x=420,y=160,speed=-3,torque=10000))
    #lb.addObject(Contacts.Contact(body1='Hero',body2='1_rotor',event_name='onRotorHit'))
    lb.addObject(Hero.HeroSprite(x=20,y=10))
    
    lb.addObject(Enemy.EnemySprite(x=325,y=25,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=400,y=25,width=32,height=32))
    
    lb.addObject(Beam.BeamSprite(x=240,y=320,width=10,height=10,static='true',angle=0).setName("hook1"))
    lb.addObject(Beam.BeamSprite(x=310,y=320,width=10,height=10,static='true',angle=0).setName("hook2"))
    lb.addObject(Enemy.EnemySprite(x=150,y=300,width=50,height=50).setName("hangman1"))
    lb.addObject(Enemy.EnemySprite(x=300,y=300,width=32,height=32).setName("hangman2"))
    
    distJoint1 = Joints.DistanceJoint(body1='hook1',body2='hangman1',damping='0.2',freq='0.8')   
    lb.addObject(distJoint1)
    
    distJoint2 = Joints.DistanceJoint(body1='hook2',body2='hangman2',damping='0.2',freq='0.8')   
    lb.addObject(distJoint2)
    
    lb.addObject(Contacts.Contact(body1='hangman1',body2='Hero',event_name='onLose'))
    lb.addObject(Contacts.Contact(body1='hangman2',body2='Hero',event_name='onLose'))
    
    
    lb.render()
