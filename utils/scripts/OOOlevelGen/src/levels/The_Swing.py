import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=33, y=36,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=238, y=147,width=281,height=14,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('swing'))
    lb.addObject(Beam.BeamSprite(x=238, y=200,width=281,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=237, y=173,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=273, y=172,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=197, y=172,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=164, y=320,width=20,height=20,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('left_hook'))
    lb.addObject(Beam.BeamSprite(x=306, y=320,width=20,height=20,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('right_hook'))
    lb.addObject(Joints.DistanceJoint(body1='left_hook',body2='swing',damping='0.2',freq='5' , b2_Xoffset = '-50' ))
    lb.addObject(Joints.DistanceJoint(body1='right_hook',body2='swing',damping='0.2',freq='5' , b2_Xoffset = '50' ))
    lb.render()