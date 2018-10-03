import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=460,y=16))
    lb.addObject(Star.StarSprite(x=16,y=16,width=32,height=32))
    
    lb.addObject(Friend.FriendSprite(x= 70 ,y=50,width=60,height=60, restitution=0.6))
    lb.addObject(Friend.FriendSprite(x=480 - 70 - 32,y=50,width=60,height=60, restitution=0.6))
    
    lb.addObject(Enemy.EnemySprite(x=140 - 32-16 ,y=320,width=150,height=150, static= 'true',restitution=0.6))
    lb.addObject(Enemy.EnemySprite(x=340 + 31 + 16,y=320,width=150,height=150,static= 'true', restitution=0.6))
    
    #lb.addObject(Beam.BeamSprite(x=100,y=140,width=280,height=30,static='true',angle=90).setName("platform"))
    
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=240,y=160,width=100,height=100,enemy_size=32))
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num2',x=140-32-16,y=160,width=100,height=100,enemy_size=32))
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num3',x=340+32+16,y=160,width=100,height=100,enemy_size=32))

    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num4',x=240 - 50,y=58,width=50,height=50,enemy_size=32))
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num5',x=240 + 50,y=58,width=50,height=50,enemy_size=32))
    
    lb.render()
