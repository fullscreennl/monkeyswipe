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
    
    lb.addObject(Launcher.LauncherSprite(name='left',x=26, y=-13, trigger_x=59, trigger_y=105))
    lb.addObject(Beam.BeamSprite(x=115, y=14,width=123,height=30,static='true',angle='0'))
    lb.addObject(Launcher.LauncherSprite(name='mid',x=205, y=-13, trigger_x=112, trigger_y=207))
    lb.addObject(Beam.BeamSprite(x=293, y=14,width=121,height=30,static='true',angle='0'))
    lb.addObject(Launcher.LauncherSprite(name='right',x=382, y=-13, trigger_x=329, trigger_y=105))
    lb.addObject(Beam.BeamSprite(x=445, y=48,width=71,height=97,static='true',angle='0'))
    lb.addObject(Beam.BeamSprite(x=459, y=310,width=127,height=44,static='true',angle='-45'))
    lb.addObject(Beam.BeamSprite(x=16, y=303,width=127,height=44,static='true',angle='45'))
    lb.addObject(Enemy.EnemySprite(x=381, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=205, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=26, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Hero.HeroSprite(x=451, y=117,width=32,height=32))
    lb.addObject(Wizard.WizardSprite(x=68,y=183))
    #lb.addObject(Enemy.EnemySprite(x=378, y=243,width=96,height=96,static='false',angle='0'))
    #lb.addObject(Star.StarSprite(x=378, y=243,width=32,height=32))
    #lb.addObject(Joints.RevoluteJoint(body1='bigboy',body2='Star',motor_speed='50',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.addObject(Enemy.EnemySprite(x=72, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=120, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=162, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=249, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=288, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=330, y=49,width=32,height=32,static='false',angle='0'))
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='cycler',x=223,y=186,width=128,height=128,enemy_size=32))
    
    lb.addObject(Star.StarSprite(x=378, y=243,width=32,height=32))
    
    lb.addObject(Enemy.EnemySprite(x=378, y=243,width=96,height=96,static='true',angle='0').setName('bigboy'))
    lb.addObject(Contacts.Contact(body1='Hero',body2=':hat_top',event_name='onReleaseStar'))
    lb.addObject(Contacts.Contact(body1='Hero',body2='bigboy',event_name='onLose'))
    revJoint = Joints.RevoluteJoint(body1='Star',body2='bigboy',motor_speed='50.0',torque='1000.0',
                                    enable_motor='false',lower_angle='12',upper_angle='45',
                                    enable_limit='false',collide_connected='false',userData='star_joint')
    lb.addObject(revJoint)
    lb.render()
