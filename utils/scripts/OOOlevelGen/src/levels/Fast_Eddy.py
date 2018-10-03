import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=146, y=2,width=100,height=100,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=326, y=148,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=326, y=204,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=18, y=19,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Hero.HeroSprite(x=456, y=22,width=32,height=32))
    lb.addObject(Star.StarSprite(x=328, y=175,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=285, y=174,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=372, y=175,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()