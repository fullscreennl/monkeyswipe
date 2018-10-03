import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=460,y=16))
    
    lb.addObject(Beam.BeamSprite(x=240,y=110,width=300,height=20,static='false',angle=0,density=1).setName("platform"))
    
   
    
    lb.addObject(Star.StarSprite(x=200,y=136,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=200,y=160,width=32,height=32, restitution=0,desity=1))
    lb.addObject(Enemy.EnemySprite(x=200-32,y=136,width=32,height=32, restitution=0,desity=1))
    lb.addObject(Enemy.EnemySprite(x=200+32,y=136,width=32,height=32, restitution=0,desity=1))
    
    lb.addObject(Friend.FriendSprite(x=280,y=136,width=32,height=32))
    lb.addObject(Friend.FriendSprite(x=280,y=160,width=32,height=32, restitution=0,desity=1))
    lb.addObject(Friend.FriendSprite(x=280-32,y=136,width=32,height=32, restitution=0,desity=1))
    lb.addObject(Friend.FriendSprite(x=280+32,y=136,width=32,height=32, restitution=0,desity=1))
    
    lb.addObject(Enemy.EnemySprite(x=240-50,y=50,width=100,height=100, restitution=0.8,desity=1))
    #lb.addObject(Enemy.EnemySprite(x=240,y=265,width=40,height=40, restitution=0,density=4))
    lb.addObject(Friend.FriendSprite(x=240+50,y=50,width=100,height=100, restitution=0.4))
    
   
    #lb.addObject(Beam.BeamSprite(x=240-137,y=200,width=60,height=10,static='true',angle=90))
    
    #lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=280,y=160,width=200,height=200,enemy_size=60))

    lb.render()
