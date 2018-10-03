import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=234, y=312,width=27,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Hook'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=27, y=174,width=59,height=59,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Hero.HeroSprite(x=19, y=18,width=32,height=32))
    lb.addObject(Star.StarSprite(x=200, y=285,width=32,height=32))
    lb.addObject(Joints.DistanceJoint(body1='Hook',body2='Star',damping='0.2',freq='5' ))
    lb.addObject(Beam.BeamSprite(x=270, y=311,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=270, y=118,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=74, y=57,width=407,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Hero.HeroSprite(x=133, y=91,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=68, y=138,width=305,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=235, y=90,width=58,height=58,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=27, y=90,width=58,height=58,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()