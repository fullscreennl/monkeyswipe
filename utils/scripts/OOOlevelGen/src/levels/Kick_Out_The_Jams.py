import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=57, y=239,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Hero.HeroSprite(x=51, y=264,width=32,height=32))
    lb.addObject(Friend.FriendSprite(x=95, y=264,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=178, y=223,width=127,height=14,angle='-15',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=415, y=30,width=61,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=450, y=27,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=353, y=280,width=68,height=68,angle='0',restitution=0.99,static='false',friction=0.5,density=5 ).setName('Enemy'))
    lb.addObject(Beam.BeamSprite(x=370, y=102,width=135,height=14,angle='135',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()