import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Enemy.EnemySprite(x=444, y=289,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Beam.BeamSprite(x=459, y=28,width=127,height=14,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=19, y=28,width=127,height=14,angle='135',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Hero.HeroSprite(x=17, y=242,width=32,height=32))
    lb.addObject(Star.StarSprite(x=405, y=299,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=62, y=291,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=444, y=135,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=23, y=121,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Enemy.EnemySprite(x=228, y=289,width=32,height=32,angle='0',restitution=0.99,static='false',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Beam.BeamSprite(x=-19, y=190,width=127,height=14,angle='-150',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()
