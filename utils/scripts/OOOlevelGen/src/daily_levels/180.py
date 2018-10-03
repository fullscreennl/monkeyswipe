import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=60, y=217,width=37,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=255, y=61,width=213,height=14,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('wipwap'))
    lb.addObject(Friend.FriendSprite(x=61, y=270,width=92,height=92,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=339, y=-10,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=338, y=91,width=47,height=47,angle='0',restitution=0.8,static='false',friction=0.5,density=5 ).setName('Enemy'))
    lb.addObject(Nut.NutSprite(x=255, y=61,width=32,height=32,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=121, y=252,width=32,height=32))
    lb.addObject(Star.StarSprite(x=293, y=84,width=32,height=32))
    lb.addObject(Joints.RevoluteJoint(body1='wipwap',body2='Nut',motor_speed='50',enable_motor='false',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.addObject(Beam.BeamSprite(x=250, y=310,width=20,height=20,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Hinge'))
    lb.addObject(Joints.DistanceJoint(body1='Hero',body2='Hinge',damping='0.2',freq='5'))
    lb.addObject(Enemy.EnemySprite(x=392, y=298,width=47,height=47,angle='0',restitution=0.8,static='true',friction=0.5,density=5 ).setName('Enemy'))
    lb.render()