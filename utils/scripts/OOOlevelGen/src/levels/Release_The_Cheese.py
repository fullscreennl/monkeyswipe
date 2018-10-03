import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=217, y=83,width=167,height=36,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Wizard.WizardSprite(x=409,y=68))
    lb.addObject(Enemy.EnemySprite(x=217, y=238,width=136,height=136,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=22, y=21,width=32,height=32))
    lb.addObject(Star.StarSprite(x=217, y=238,width=32,height=32))
    lb.addObject(Contacts.Contact(body1='Hero',body2=':hat_top',event_name='onReleaseStar'))
    lb.addObject(Joints.RevoluteJoint(body1='Enemy',body2='Star',motor_speed='1',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',userData='star_joint',enable_limit='false',collide_connected='false'))
    lb.render()