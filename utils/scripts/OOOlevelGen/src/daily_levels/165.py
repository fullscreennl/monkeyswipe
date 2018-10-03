import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Beam.BeamSprite(x=145, y=259,width=316,height=42,static='true',angle='-15'))
    lb.addObject(Enemy.EnemySprite(x=212, y=291,width=54,height=54,static='false',angle='0'))
    lb.addObject(Beam.BeamSprite(x=347, y=127,width=316,height=41,static='true',angle='24'))
    lb.addObject(Enemy.EnemySprite(x=449, y=224,width=54,height=54,static='false',angle='0'))
    lb.addObject(Enemy.EnemySprite(x=396, y=201,width=54,height=54,static='false',angle='0'))
    lb.addObject(Hero.HeroSprite(x=463, y=16,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=396, y=28,width=54,height=54,static='false',angle='0'))
    lb.addObject(Star.StarSprite(x=16, y=17,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=90, y=62,width=164,height=41,static='true',angle='105'))

    
    lb.render()
