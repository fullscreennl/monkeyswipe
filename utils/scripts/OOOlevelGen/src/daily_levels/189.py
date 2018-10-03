import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Rotor.RotorSprite(x=61,y=59,speed=11,angle=0,torque=1000))
    lb.addObject(Rotor.RotorSprite(x=168,y=59,speed=9,angle=0,torque=1000))
    lb.addObject(Rotor.RotorSprite(x=275,y=59,speed=10,angle=0,torque=1000))
    lb.addObject(Rotor.RotorSprite(x=425,y=59,speed=10,angle=0,torque=1000))
    lb.addObject(Enemy.EnemySprite(x=380, y=194,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=459, y=292,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=458, y=256,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=303, y=194,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Star.StarSprite(x=348, y=13,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=341, y=196,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=346, y=171,width=101,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=458, y=218,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.render()
