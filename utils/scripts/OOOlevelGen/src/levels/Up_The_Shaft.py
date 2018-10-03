import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='cycler',x=302,y=158,width=206,height=206,enemy_size=32))
    lb.addObject(Enemy.EnemySprite(x=304, y=28,width=53,height=53,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Hero.HeroSprite(x=78, y=20,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=467, y=265,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=521, y=212,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=405, y=289,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=462, y=237,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=-10, y=64,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=47, y=133,width=127,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=109, y=133,width=127,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=78, y=218,width=63,height=63,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=130, y=64,width=56,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()