import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Rotor.RotorSprite(x=50,y=71,speed=11,angle=0,torque=1000))
    lb.addObject(Rotor.RotorSprite(x=157,y=71,speed=9,angle=0,torque=1000))
    lb.addObject(Rotor.RotorSprite(x=264,y=71,speed=10,angle=0,torque=1000))
    lb.addObject(Rotor.RotorSprite(x=414,y=71,speed=10,angle=0,torque=1000))
    lb.addObject(Enemy.EnemySprite(x=369, y=206,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=448, y=304,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=447, y=268,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=292, y=206,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Star.StarSprite(x=337, y=25,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=330, y=208,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=335, y=183,width=101,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=447, y=230,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.render()
