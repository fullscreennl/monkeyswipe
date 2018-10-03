import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=308, y=19,width=32,height=32))
    lb.addObject(Star.StarSprite(x=16, y=16,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=160, y=161,width=320,height=320,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=371, y=124,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('EnemySmall'))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=422, y=19,width=40,height=40,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Joints.DistanceJoint(body1='EnemySmall',body2='Spikey',damping='0.2',freq='5'))
    lb.addObject(Joints.DistanceJoint(body1='EnemySmall',body2='Hero',damping='0.2',freq='5'))
    lb.render()