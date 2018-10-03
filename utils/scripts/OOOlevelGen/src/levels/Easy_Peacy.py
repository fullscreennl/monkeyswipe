import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=240, y=63,width=127,height=46,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=240, y=208,width=162,height=162,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=31, y=26,width=32,height=32))
    lb.addObject(Star.StarSprite(x=450, y=25,width=32,height=32))
    lb.render()
