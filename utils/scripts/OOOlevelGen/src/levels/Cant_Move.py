import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=116, y=30,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Star.StarSprite(x=409, y=134,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=48, y=31,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=48, y=73,width=17,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('HeroHook'))
    lb.addObject(Joints.DistanceJoint(body1='Hero',body2='HeroHook',damping='0.2',freq='5' ))
    lb.addObject(Beam.BeamSprite(x=409, y=110,width=39,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=462, y=22,width=89,height=14,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=211, y=110,width=39,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=210, y=135,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=350, y=110,width=39,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=350, y=135,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=268, y=110,width=39,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=268, y=135,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()