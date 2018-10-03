import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=43, y=35,width=75,height=14,angle='-45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=10, y=63,width=127,height=22,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=235, y=7,width=459,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=24, y=63,width=41,height=14,angle='-66',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=65, y=17,width=41,height=14,angle='-36',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=74, y=14,width=41,height=14,angle='-21',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=17, y=83,width=41,height=14,angle='-81',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=32, y=48,width=41,height=14,angle='-51',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=84, y=10,width=41,height=14,angle='-12',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=412, y=33,width=74,height=13,angle='-134',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=459, y=63,width=127,height=52,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=430, y=61,width=41,height=13,angle='-113',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=390, y=15,width=41,height=13,angle='-143',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=382, y=11,width=40,height=13,angle='-159',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=436, y=80,width=42,height=13,angle='-99',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=422, y=46,width=41,height=13,angle='-128',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=372, y=8,width=40,height=14,angle='-168',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Hero.HeroSprite(x=17, y=151,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=415, y=301,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=459, y=143,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=415, y=263,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=415, y=226,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=227,y=255,scaling=1,speed=3000,torque=3))
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=227,y=123,scaling=1,speed=2,torque=3000))
    lb.addObject(Friend.FriendSprite(x=416, y=188,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()