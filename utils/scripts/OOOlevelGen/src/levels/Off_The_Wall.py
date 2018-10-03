import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=460,y=16))
    lb.addObject(Star.StarSprite(x=16,y=16,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=32,y=200,width=32,height=32, restitution=0.6))
    
    lb.addObject(Beam.BeamSprite(x=100,y=140,width=280,height=30,static='true',angle=90).setName("platform"))
    
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=280,y=160,width=200,height=200,enemy_size=60))

    lb.render()
