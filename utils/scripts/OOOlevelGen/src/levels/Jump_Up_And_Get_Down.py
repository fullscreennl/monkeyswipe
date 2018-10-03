import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Rotor.RotorSprite(x=240,y=164,speed=10,angle=0,torque=2000))
    lb.addObject(Beam.BeamSprite(x=81, y=246,width=190,height=14,angle='-7',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=28, y=281,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=81, y=276,width=32,height=32,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=119, y=269,width=32,height=32,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=160, y=262,width=32,height=32,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Hero.HeroSprite(x=24, y=31,width=32,height=32))
    lb.render()