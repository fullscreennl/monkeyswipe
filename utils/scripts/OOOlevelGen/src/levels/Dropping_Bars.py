import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=182, y=31,width=61,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=203, y=41,width=81,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=225, y=50,width=99,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=246, y=62,width=123,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=267, y=73,width=145,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=129, y=17,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=300, y=19,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=37, y=21,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=341, y=19,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=300, y=56,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=267, y=162,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()