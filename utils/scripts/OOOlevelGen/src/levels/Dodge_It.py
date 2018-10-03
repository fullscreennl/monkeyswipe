import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=203, y=111,width=407,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=466, y=13,width=127,height=14,angle='30',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=446, y=303,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.1,density=20 ).setName('Enemy'))
    lb.addObject(Hero.HeroSprite(x=18, y=22,width=32,height=32))
    lb.addObject(Star.StarSprite(x=15, y=138,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=400, y=181,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=446, y=73,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.1,density=20 ).setName('Enemy'))
    lb.render()