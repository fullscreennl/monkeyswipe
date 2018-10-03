import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Bomb.BombSprite(x=227, y=15,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=227, y=82,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=14, y=15,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=227, y=162,width=122,height=122,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=200, y=51,width=103,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=253, y=69,width=67,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Bomb.BombSprite(x=227, y=49,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()
