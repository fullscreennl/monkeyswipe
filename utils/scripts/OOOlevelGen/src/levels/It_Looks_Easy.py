import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Enemy.EnemySprite(x=340, y=49,width=99,height=99,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=240, y=106,width=317,height=14,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=249, y=20,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=74, y=14,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=170, y=49,width=99,height=99,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=252, y=176,width=127,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=252, y=257,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()
