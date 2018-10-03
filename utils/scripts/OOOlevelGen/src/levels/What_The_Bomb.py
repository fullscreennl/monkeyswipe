import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=262, y=2,width=552,height=14,angle='1',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Hero.HeroSprite(x=155, y=20,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=303, y=84,width=552,height=14,angle='1',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Bomb.BombSprite(x=414, y=46,width=63,height=63 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=41, y=86,width=26,height=12,angle='-24',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=58, y=161,width=18,height=18))
    lb.addObject(Enemy.EnemySprite(x=464, y=28,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()