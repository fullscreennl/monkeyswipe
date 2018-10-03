import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=86, y=36,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=125, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=174, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=205, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=239, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=271, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=316, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=360, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Hero.HeroSprite(x=341, y=164,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=339, y=312,width=25,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Joints.DistanceJoint(body1='Beam',body2='Hero',damping='0.2',freq='2' ))
    lb.addObject(Star.StarSprite(x=300, y=48,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=335, y=43,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=182, y=69,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=448, y=36,width=127,height=14,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam_2'))
    lb.addObject(Beam.BeamSprite(x=37, y=36,width=127,height=14,angle='-45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam_2'))
    lb.render()