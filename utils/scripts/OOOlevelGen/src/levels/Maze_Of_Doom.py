import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=16,y=16))
    lb.addObject(Star.StarSprite(x=450,y=16,width=32,height=32))

    for e in range(10):
        if e not in (8,9):
            lb.addObject(Enemy.EnemySprite(x=100,y=16+(e*32),width=32,height=32,density='1',static='true'))
    for e in range(10):
        if e not in (1,2):
            lb.addObject(Enemy.EnemySprite(x=200,y=16+(e*32),width=32,height=32,density='1',static='true'))
    for e in range(10):
        if e not in (7,8):
            lb.addObject(Enemy.EnemySprite(x=300,y=16+(e*32),width=32,height=32,density='1',static='true'))
    for e in range(10):
        if e not in (3,4):
            lb.addObject(Enemy.EnemySprite(x=400,y=16+(e*32),width=32,height=32,density='1',static='true'))
    lb.render()
