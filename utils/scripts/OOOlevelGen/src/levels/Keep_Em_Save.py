import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=19, y=27,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=457, y=27,width=32,height=32))
    lb.addObject(Star.StarSprite(x=237, y=90,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=237, y=37,width=74,height=74,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=237, y=143,width=74,height=74,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=237, y=217,width=74,height=74,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=237, y=270,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()