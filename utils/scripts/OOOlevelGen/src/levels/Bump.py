import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=231, y=312,width=25,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Friend.FriendSprite(x=230, y=138,width=264,height=264,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Friend'))
    lb.addObject(Joints.DistanceJoint(body1='Beam',body2='Friend',damping='0.2',freq='30' ))
    lb.addObject(Hero.HeroSprite(x=32, y=24,width=32,height=32))
    lb.addObject(Star.StarSprite(x=460, y=22,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=394, y=118,width=234,height=14,angle='90',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Beam2'))
    lb.addObject(Enemy.EnemySprite(x=394, y=276,width=79,height=79,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()
