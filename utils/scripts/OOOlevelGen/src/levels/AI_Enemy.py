import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Friend.FriendSprite(x=213, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=331, y=140,width=279,height=279,angle='0',restitution=0.5,static='false',friction=0.5,density=5 ).setName('Enemy'))
    lb.addObject(Star.StarSprite(x=462, y=17,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=18, y=16,width=32,height=32))
    lb.addObject(Joints.RevoluteJoint(body1='Enemy',body2='Friend',motor_speed='50',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.render()
