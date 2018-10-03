import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Joints.PrismaticJoint(body1='Spikey',motor_speed='50',enable_motor='false',torque='1000',lower_translation='12',upper_translation='400',enable_limit='true',vertical='true'))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=101, y=72,width=40,height=40,restitution=0.2,static='false',friction=0.5,density=20 ).setName('Spikey'))
    lb.addObject(Hero.HeroSprite(x=101, y=16,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=141, y=289,width=60,height=60,angle='0',restitution=1,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Friend.FriendSprite(x=348, y=291,width=32,height=32,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Joints.DistanceJoint(body1='Enemy',body2='Friend',damping='0.2',freq='30' ))
    lb.addObject(Star.StarSprite(x=141, y=289,width=32,height=32))
    lb.addObject(Joints.RevoluteJoint(body1='Star',body2='Enemy',motor_speed='1',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',userData='rev_joint',enable_limit='false',collide_connected='false'))
    lb.render()
