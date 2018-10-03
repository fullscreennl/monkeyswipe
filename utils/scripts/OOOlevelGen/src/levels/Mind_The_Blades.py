import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Rotor.RotorSprite(x=185,y=172,speed=5,angle=0,torque=1000))
    lb.addObject(Hero.HeroSprite(x=21, y=26,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=141, y=292,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=391, y=291,width=58,height=58,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=447, y=269,width=65,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=456, y=294,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=54, y=172,width=140,height=19,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=380, y=172,width=275,height=19,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()
