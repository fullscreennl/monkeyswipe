import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=119, y=63,width=127,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=119, y=145,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=230, y=63,width=127,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=230, y=145,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=342, y=63,width=127,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=342, y=145,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=284, y=188,width=393,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Friend.FriendSprite(x=267, y=256,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=274, y=247,width=57,height=57,angle='0',restitution=0.5,static='false',friction=0.5,density=5 ).setName('Enemy'))
    lb.addObject(Star.StarSprite(x=445, y=211,width=32,height=32))
    lb.addObject(Joints.RevoluteJoint(body1='Enemy',body2='Friend',motor_speed='50',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',userData='rev_joint',enable_limit='false',collide_connected='false'))
    lb.addObject(Hero.HeroSprite(x=444, y=22,width=32,height=32))
    lb.render()