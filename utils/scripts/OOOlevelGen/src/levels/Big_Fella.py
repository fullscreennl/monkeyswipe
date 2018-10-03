import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Friend.FriendSprite(x=263, y=142,width=268,height=268,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=263, y=303,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=432, y=26,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=29, y=21,width=32,height=32))
    lb.render()
