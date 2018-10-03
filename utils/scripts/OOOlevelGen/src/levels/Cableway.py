import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=240,y=160))
    lb.addObject(Beam.BeamSprite(x=240,y=290,width=480,height=10,static='true',angle=0,density=4))
    
    
    lb.addObject(Enemy.EnemySprite(x=240-20,y=310,width=20,height=20).setName('wheel1'))
    lb.addObject(Enemy.EnemySprite(x=240+20,y=310,width=20,height=20).setName('wheel2'))
    
    distJoint1 = Joints.DistanceJoint(body1="wheel1",body2="Hero",damping='10',freq='0')
    distJoint2 = Joints.DistanceJoint(body1="wheel2",body2="Hero",damping='10',freq='0')
    distJoint3 = Joints.DistanceJoint(body1="wheel2",body2="wheel1",damping='10',freq='0')
    lb.addObject(distJoint1)
    lb.addObject(distJoint2)
    lb.addObject(distJoint3)
    
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=100,width=32,height=32,density=6,restitution=0.6))
    distJoint4 = Joints.DistanceJoint(body1="Hero",body2="Spikey",damping='10',freq='0')
    lb.addObject(distJoint4)
    
    lb.addObject(Wizard.WizardSprite(x=25,y=100));
    lb.addObject(Contacts.Contact(body1='Hero',body2=':hat_top',event_name='onReleaseStar'))
    
    lb.addObject(Enemy.EnemySprite(x=400,y=200,width=40,height=40))
    lb.addObject(Enemy.EnemySprite(x=75,y=200,width=40,height=40))
    
    lb.addObject(Enemy.EnemySprite(x=460,y=260,width=40,height=40,static='true').setName('Holder'))
    lb.addObject(Star.StarSprite(x=460,y=260,width=32,height=32))
    revJoint = Joints.RevoluteJoint(body1='Star',body2='Holder',motor_speed='50.0',torque='1000.0',
                                    enable_motor='false',lower_angle='12',upper_angle='45',
                                    enable_limit='false',collide_connected='false',userData='star_joint')
    lb.addObject(revJoint)
    
    lb.addObject(Beam.BeamSprite(x=480-(100/2),y=130,width=100,height=10,static='true',angle=0,density=4))
    lb.addObject(Beam.BeamSprite(x=75,y=130,width=50,height=10,static='true',angle=0,density=4))
    lb.addObject(Beam.BeamSprite(x=25,y=15,width=50,height=30,static='true',angle=0,density=4))
    #lb.addObject(Enemy.EnemySprite(x=280,y=25,width=50,height=50))
    lb.render()
