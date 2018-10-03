import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=33, y=19,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=161, y=19,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=305, y=19,width=32,height=32))
    lb.addObject(Star.StarSprite(x=427, y=16,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=365, y=63,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=34, y=53,width=32,height=32,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=161, y=53,width=32,height=32,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=194, y=19,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=20, y=278,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Beam.BeamSprite(x=55, y=255,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()