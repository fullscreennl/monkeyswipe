import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=460,y=240))
    
    for i in range(15):
        lb.addObject(Enemy.EnemySprite(x=10*i,y=50,width=15,height=15, restitution=0,desity=3))
        
    #for i in range(15):
    #    lb.addObject(Enemy.EnemySprite(x=10*i,y=100,width=15,height=15, restitution=0,desity=3))
        
    for k in range(5):
        lb.addObject(Bomb.BombSprite(x=32*k,y=120,width=32,height=32,static='false'))
        
    lb.addObject(Beam.BeamSprite(x=240,y=0,height=20,width=320,static='true',angle=90))
        
    #for j in range(5):
    #    lb.addObject(Friend.FriendSprite(x=32*j,y=200,width=32,height=32, restitution=0,desity=3))
        
    lb.addObject(Star.StarSprite(x=20,y=16,width=32,height=32))
    
    lb.render()
