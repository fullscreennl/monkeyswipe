import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Enemy.EnemySprite(x=231, y=13,width=244,height=244,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Beam.BeamSprite(x=121, y=270,width=355,height=14,angle='-4',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=16, y=298,width=18,height=18))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=229, y=153,width=32,height=32,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Hero.HeroSprite(x=60, y=28,width=32,height=32))
    lb.addObject(Joints.DistanceJoint(body1='Hook',body2='Hero',damping='0.2',freq='30' ))
    lb.addObject(Star.StarSprite(x=137, y=293,width=18,height=18))
    lb.addObject(Star.StarSprite(x=282, y=280,width=18,height=18))
    lb.addObject(Beam.BeamSprite(x=59, y=89,width=10,height=10,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Hook'))
    lb.addObject(Beam.BeamSprite(x=395, y=91,width=85,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()