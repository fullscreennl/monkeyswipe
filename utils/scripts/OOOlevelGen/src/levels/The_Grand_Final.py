import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=160,y=40))
    
    lb.addObject(EnemyBucketWithStar.EnemyBucketWithStarSprite(width=150,height=100, x=240, y=160, num_enemies=30, enemy_size=20))
    
    lb.addObject(Beam.BeamSprite(x=240,y=160,width=10,height=10,static='true',angle=0).setName("platform"))
    
    
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=240,y=250,scaling=1.0,speed=3,torque=10000))
    
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=65,y=160,width=80,height=80,enemy_size=20))
    #lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num2',x=420,y=160,width=80,height=80,enemy_size=20))

    distJoint = Joints.DistanceJoint(body1="Bomb",body2="platform",damping='10',freq='0')
    lb.addObject(distJoint)

    lb.addObject(Friend.FriendSprite(x=300,y=125,width=64,height=64,denstity=0.02))
    
    lb.addObject(Beam.BeamSprite(x=480,y=-100,width=200,height=200,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=0,y=-100,width=240,height=240,static='true',angle=60))
    
    lb.addObject(Wizard.WizardSprite(x=450,y=160));
    lb.addObject(Contacts.Contact(body1='Hero',body2=':hat_top',event_name='onReleaseStar'))
    
    lb.addObject(Enemy.EnemySprite(x=240,y=160,width=50,height=50,restitution=0.8,static='false').setName('StarHolder'))
    
    revJoint = Joints.RevoluteJoint(body1='Star',body2='StarHolder',motor_speed='50.0',torque='1000.0',
                                    enable_motor='true',lower_angle='12',upper_angle='45',
                                    enable_limit='false',collide_connected='false',userData='star_joint')
    lb.addObject(revJoint)
    
    lb.addObject(Contacts.Contact(body1='StarHolder',body2='Hero',event_name='onLose'))
    
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=20,y=40,width=40,height=40,density=6,restitution=0.6))
    
    lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=400, y=-15, trigger_x=100, trigger_y=300))
    
    lb.addObject(Rotor.RotorSprite(x=420,y=260,speed=5,torque=10000))
    #lb.addObject(Rotor.RotorSprite(x=180,y=160,speed=1,torque=10000))
    
    lb.addObject(Bomb.BombSprite(x=240,y=40,width=32,height=32,static='false'))
    
    #lb.addObject(Nut.NutSprite(x=32,y=272, eventName='onNutHitAll'))

    lb.render()
