import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=42, y=245,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=42, y=287,width=17,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('HeroHook'))
    lb.addObject(Joints.DistanceJoint(body1='Hero',body2='HeroHook',damping='0.2',freq='5' ))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=460, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Star.StarSprite(x=364, y=264,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=239, y=239,width=282,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=306, y=99,width=282,height=14,angle='14',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=252, y=-1,width=282,height=14,angle='-10',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=271, y=169,width=229,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=394, y=172,width=33,height=14,angle='15',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=239, y=293,width=282,height=14,angle='2',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=375, y=310,width=8,height=8,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=-21, y=12,width=282,height=14,angle='5',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()