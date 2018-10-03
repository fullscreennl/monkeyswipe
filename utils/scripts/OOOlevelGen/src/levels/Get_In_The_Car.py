import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=245, y=17,width=127,height=14,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=182, y=17,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=308, y=17,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=235, y=232,width=82,height=82,angle='0',restitution=0.8,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Star.StarSprite(x=33, y=22,width=32,height=32))
    lb.addObject(Joints.RevoluteJoint(body1='Hero',body2='Beam',motor_speed='50',enable_motor='false',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.addObject(Joints.RevoluteJoint(body1='Friend',body2='Beam',motor_speed='50',enable_motor='false',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.render()