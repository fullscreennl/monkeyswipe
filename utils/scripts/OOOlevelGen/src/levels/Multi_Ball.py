import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=187, y=43,width=87,height=26,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=272, y=43,width=87,height=26,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=228, y=29,width=32,height=32))
    lb.addObject(Bomb.BombSprite(x=230, y=132,width=104,height=104 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=230, y=204,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=230, y=246,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=230, y=292,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=17, y=23,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=68, y=21,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=121, y=25,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=331, y=25,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=382, y=23,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=435, y=27,width=32,height=32))
    lb.render()
