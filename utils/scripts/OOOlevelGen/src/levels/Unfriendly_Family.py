import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=240,y=10))
    lb.addObject(Beam.BeamSprite(x=240+32,y=30,width=60,height=30,static='false',angle=90))
    lb.addObject(Beam.BeamSprite(x=240-32,y=30,width=60,height=30,static='true',angle=90))
    lb.addObject(Enemy.EnemySprite(x=240,y=200,width=50,height=50))
    lb.addObject(Enemy.EnemySprite(x=240,y=225,width=50,height=50))
    for i in range(5):
        lb.addObject(Enemy.EnemySprite(x=240,y=300,width=20,height=20))
    lb.addObject(Enemy.EnemySprite(x=240,y=125,width=128,height=128,denstity=0.1))
    lb.addObject(Star.StarSprite(x=180,y=10,width=20,height=20))
    lb.render()
