import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=240,y=240))
    
    for i in range(15):
        lb.addObject(Enemy.EnemySprite(x=32*i,y=50,width=32,height=32, restitution=0,desity=3))
        
    for k in range(15):
        lb.addObject(Bomb.BombSprite(x=32*k,y=120,width=32,height=32,static='false'))
        
    for j in range(13):
        lb.addObject(Friend.FriendSprite(x=32*j,y=200,width=32,height=32, restitution=0,desity=3))
        
    

    lb.addObject(Star.StarSprite(x=240,y=16,width=32,height=32))
    
    lb.render()
