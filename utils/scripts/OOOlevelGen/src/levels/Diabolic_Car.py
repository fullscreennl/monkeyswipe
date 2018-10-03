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
    #lb.addObject(Hero.HeroSprite(x=22,y=16))
    beamwidth=380
    lb.addObject(Beam.BeamSprite(x=beamwidth/2,y=108,width=beamwidth,height=10,static='true',angle=0))
    lb.addObject(Beam.BeamSprite(x=480 - beamwidth/2,y=216,width=beamwidth,height=10,static='true',angle=0))
    #lb.addObject(Beam.BeamSprite(x=210,y=170,width=60,height=30,static='true',angle=0))
    #lb.addObject(Friend.FriendSprite(x=260,y=16,width=5,height=5, density=1)) 
    offsetx=480 - 100
    offsety=230
    
    enemyrad=20
    restitute=1
    lb.addObject(Enemy.EnemySprite(x=36/2+offsetx,y=20/2+offsety,width=enemyrad,height=enemyrad,density=1,restitution=restitute).setName('v1')) 
    lb.addObject(Enemy.EnemySprite(x=124/2+offsetx,y=20/2+offsety,width=enemyrad,height=enemyrad,density=1,restitution=restitute).setName('v2'))
    lb.addObject(Enemy.EnemySprite(x=152/2+offsetx,y=114/2+offsety,width=enemyrad,height=enemyrad,density=1,restitution=restitute).setName('v3')) 
    lb.addObject(Enemy.EnemySprite(x=8/2+offsetx,y=114/2+offsety,width=enemyrad,height=enemyrad,density=1,restitution=restitute).setName('v5')) 
    lb.addObject(Enemy.EnemySprite(x=80/2+offsetx,y=158/2+offsety,width=enemyrad,height=enemyrad,density=1,restitution=restitute).setName('v4')) 
    lb.addObject(Friend.FriendSprite(x=80/2+offsetx,y=80/2+offsety,width=10,height=10,density=1))
    lb.addObject(Hero.HeroSprite(x=80/2+offsetx,y=80/2+offsety,width=32,height=32))
     
    lb.addObject(Star.StarSprite(x=20,y=16,width=32,height=32,restitution=0.95,density=2))
    
    #dampV='0.2'
    #freqV='5'
    
    dampV='1.2'
    freqV='25'
    
    distJoint = Joints.DistanceJoint(body1='v1',body2='v3',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v1',body2='v4',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v2',body2='v4',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v2',body2='v5',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v3',body2='v5',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    
    distJoint = Joints.DistanceJoint(body1='v1',body2='Friend',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v2',body2='Friend',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v3',body2='Friend',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v4',body2='Friend',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='v5',body2='Friend',damping=dampV,freq=freqV)   
    lb.addObject(distJoint)    
    lb.addObject(Contacts.Contact(body1='Hero',body2='v1',event_name='onLose'))
    lb.addObject(Contacts.Contact(body1='Hero',body2='v2',event_name='onLose')) 
    lb.addObject(Contacts.Contact(body1='Hero',body2='v3',event_name='onLose'))	
    lb.addObject(Contacts.Contact(body1='Hero',body2='v4',event_name='onLose'))	 
    lb.addObject(Contacts.Contact(body1='Friend',body2='v5',event_name='onLose'))	 
    distJoint = Joints.DistanceJoint(body1='Hero',body2='Friend',damping=dampV,freq=freqV)   
    lb.addObject(distJoint) 
    
    #distJoint = Joints.DistanceJoint(body1='Hero',body2='Friend',damping='0.2',freq='4')  
    #lb.addObject(distJoint)
    
    #lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=200,y=20,width=40,height=40))
    lb.render()
