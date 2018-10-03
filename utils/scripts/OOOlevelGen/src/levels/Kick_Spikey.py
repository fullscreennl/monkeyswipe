import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Enemy.EnemySprite(x=328, y=151,width=300,height=300,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=455, y=22,width=32,height=32))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=129, y=147,width=40,height=40,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=11, y=22,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=129, y=299,width=10,height=10,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Joints.DistanceJoint(body1='Beam',body2='Spikey',damping='0.2',freq='5' ))
    lb.render()
