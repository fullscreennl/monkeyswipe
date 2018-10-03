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
    lb.addObject(Hero.HeroSprite(x=20,y=10))
    lb.addObject(Star.StarSprite(x=420,y=50,width=30,height=30))
    
    
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=200,width=40,height=40,density=6,restitution=0.6))
    
    for i in range(15):
        lb.addObject(Enemy.EnemySprite(x=450,y=250,width=30,height=30))
    
    #distJoint = Joints.DistanceJoint(body1='Spikey',body2='Nut',damping='10.0',freq='0.0') 
    
    lb.addObject(Beam.BeamSprite(x=350,y=0,width=300,height=30,static='true',angle=90))
    lb.addObject(Friend.FriendSprite(x=350,y=150,width=40,height=40,static='true'))
    lb.addObject(Beam.BeamSprite(x=395,y=0,width=65,height=60,static='true',angle=0))
    
    lb.addObject(Beam.BeamSprite(x=200,y=0,width=50,height=50,static='true',angle=45))
    
    lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=455, y=-15, trigger_x=100, trigger_y=300))
    #lb.addObject(Wizard.WizardSprite(x=25,y=50))  
    #lb.addObject(distJoint)
    lb.render()
