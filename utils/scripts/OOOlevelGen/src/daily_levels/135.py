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
    
    
    # CHAIN #
    lb.addObject(Beam.BeamSprite(x=10,y=200,width=20,height=15,static='true',angle=0).setName("filler"))
    lb.addObject(Beam.BeamSprite(x=25,y=200,width=15,height=15,static='true',angle=0).setName("pole_left"))
    lb.addObject(Beam.BeamSprite(x=443,y=150,width=15,height=35,static='true',angle=20).setName("pole_right"))

    #lb.addObject(Bomb.BombSprite(x=180,y=16,width=32,height=32,static='false'))

    prevbody = "pole_left"
    types = [0,0,0,0,0,0,0,0,0,0]
    e = 0
    for t in types:
        if not t:
            lb.addObject(Enemy.EnemySprite(x=50 + (e*40),y=180,width=32,height=32, density=1, friction=200,static='false').setName("e"+str(e)))
            lb.addObject(Contacts.Contact(body1='Hero',body2='e'+str(e),event_name='onLose'))
        else:
            lb.addObject(Friend.FriendSprite(x=50 + (e*40),y=180,width=40,height=40, density=1, friction=200,static='false').setName("e"+str(e)))
        currentbody = "e"+str(e)
        distJoint = Joints.DistanceJoint(body1=prevbody,body2=currentbody,damping='10',freq='15')
        prevbody = currentbody
        lb.addObject(distJoint)
        e = e+1
        
    #lb.addObject(Beam.BeamSprite(x=200,y=0,width=50,height=50,static='true',angle=45))
    #lb.addObject(Friend.FriendSprite(x=400,y=20,width=40,height=40, density=1, friction=10,static='false'))

    distJoint = Joints.DistanceJoint(body1=prevbody,body2="pole_right",damping='10',freq='15')
    lb.addObject(distJoint)
    
    # END CHAIN#
   
    
    #lb.addObject(Enemy.EnemySprite(x=240,y=200,width=50,height=50,restitution=0.8,static='true').setName("star_holder"))
    
    lb.addObject(Star.StarSprite(x=240,y=300,width=20,height=20))
    
    revJoint = Joints.RevoluteJoint(body1='Star',body2='star_holder',motor_speed='50.0',torque='500.0',
                                    enable_motor='false',lower_angle='12',upper_angle='45',
                                    enable_limit='false',collide_connected='false',userData='star_joint')
    
    #lb.addObject(revJoint)
    
    #lb.addObject(Enemy.EnemySprite(x=240,y=200,width=100,height=100,restitution=0.8,static='true'))
    #lb.addObject(Enemy.EnemySprite(x=240,y=200,width=128,height=128,restitution=0.8,static='true'))
    
    lb.addObject(Friend.FriendSprite(x=100,y=20,width=40,height=40,density=10))
    
    #lb.addObject(Friend.FriendSprite(x=140,y=60,width=120,height=120,density=100, friction=200,static='false'))
    #lb.addObject(Friend.FriendSprite(x=340,y=60,width=120,height=120, density=100,friction=200,static='false'))
    #lb.addObject(Enemy.EnemySprite(x=190,y=158,width=100,height=100, density=1, friction=200,static='false'))
    #lb.addObject(Enemy.EnemySprite(x=290,y=158,width=100,height=100, density=1, friction=200,static='false'))
    #lb.addObject(Enemy.EnemySprite(x=240,y=215,width=50,height=50, density=1, friction=200,static='false'))
    lb.addObject(Beam.BeamSprite(x=184,y=15,width=60,height=30,static='true',angle=0))
    lb.addObject(Beam.BeamSprite(x=296,y=15,width=60,height=30,static='true',angle=0))
    
    lb.addObject(Beam.BeamSprite(x=118,y=-43,width=120,height=120,static='true',angle=15))
    lb.addObject(Beam.BeamSprite(x=390,y=-2,width=200,height=120,static='true',angle=15))
    #lb.addObject(Beam.BeamSprite(x=296,y=15,width=60,height=60,static='true',angle=0))
    
    lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=240, y=-15, trigger_x=40, trigger_y=100,power='#500'))
    
    #lb.addObject(Contacts.Contact(body1='Spikey',body2='star_holder',event_name='onDestroy'))
    lb.addObject(Contacts.Contact(body1='Hero',body2='star_holder',event_name='onLose'))
    
    lb.render()
