import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=418, y=157,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=373, y=180,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=414, y=180,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=416, y=221,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=475, y=168,width=33,height=19,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=248, y=-4,width=61,height=56,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Friend.FriendSprite(x=365, y=24,width=32,height=32,angle='0',restitution=0.6,static='false',friction=0.5,density=20 ).setName('Friend'))
    lb.addObject(Hero.HeroSprite(x=32, y=22,width=32,height=32))
    lb.render()
