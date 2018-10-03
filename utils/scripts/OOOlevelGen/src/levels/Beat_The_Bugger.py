import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=22, y=277,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=22, y=252,width=45,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=93, y=185,width=272,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=22, y=194,width=45,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=29, y=219,width=40,height=40,restitution=0.5,static='false',friction=0.5,density=20 ).setName('Spikey'))
    lb.addObject(Enemy.EnemySprite(x=43, y=37,width=74,height=74,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=212, y=0,width=50,height=50,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=305, y=121,width=248,height=248,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=453, y=21,width=32,height=32))
    lb.render()
