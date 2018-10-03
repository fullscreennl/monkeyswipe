import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=183, y=44,width=89,height=14,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=80, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=183, y=106,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=259, y=71,width=142,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=259, y=161,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=259, y=253,width=142,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=448, y=22,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=21, y=14,width=32,height=32))
    lb.addObject(Rotor.RotorSprite(x=116,y=214,speed=5,angle=0,torque=1000))
    lb.render()