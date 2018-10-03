import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=147, y=261,width=306,height=14,angle='-4',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=23, y=297,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=238, y=165,width=201,height=14,angle='56',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=285, y=125,width=342,height=14,angle='56',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=451, y=260,width=154,height=14,angle='-4',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=315, y=227,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=273, y=278,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=447, y=291,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=23, y=24,width=32,height=32))
    lb.render()