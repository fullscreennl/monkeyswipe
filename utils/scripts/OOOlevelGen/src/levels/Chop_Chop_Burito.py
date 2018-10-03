import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=16,y=16))
    lb.addObject(Star.StarSprite(x=240,y=300,width=32,height=32))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=160,width=32,height=32,density='1',restitution='0.7'))

    lb.addObject(Beam.BeamSprite(x=240,y=0,width=50,height=50,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=0,y=0,width=30,height=30,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=480,y=0,width=30,height=30,static='true',angle=45))

    for e in range(15):
        if e not in (7,8):
            lb.addObject(Enemy.EnemySprite(y=280,x=16+(e*32),width=32,height=32,density='1',static='true'))
    for e in range(15):
        lb.addObject(Enemy.EnemySprite(y=250,x=16+(e*32),width=32,height=32,density='1',static='true'))
    for e in range(15):
        if e not in (7,8):
            lb.addObject(Enemy.EnemySprite(y=150,x=16+(e*32),width=32,height=32,density='1',static='true'))
    for e in range(15):
        if e not in (3,4):
            lb.addObject(Enemy.EnemySprite(y=50,x=16+(e*32),width=32,height=32,density='1',static='true'))
    lb.render()
