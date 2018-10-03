import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Friend.FriendSprite(classname = 'AccelFriendSprite', x=24, y=148,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Beam.BeamSprite(x=193, y=124,width=407,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=127, y=148,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=30, y=27,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=193, y=174,width=407,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=163, y=147,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=213, y=147,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=265, y=147,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=318, y=147,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=359, y=147,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()