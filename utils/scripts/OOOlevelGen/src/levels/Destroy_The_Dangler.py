import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=353, y=310,width=20,height=20,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Beam_right'))
    lb.addObject(Beam.BeamSprite(x=117, y=310,width=20,height=20,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Beam_left'))
    lb.addObject(Enemy.EnemySprite(x=430, y=168,width=96,height=96,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=430, y=168,width=32,height=32))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=24, y=172,width=40,height=40,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=191, y=21,width=32,height=32))
    lb.addObject(Joints.RevoluteJoint(body1='Enemy',body2='Star',motor_speed='50',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.addObject(Joints.DistanceJoint(body1='Beam_right',body2='Enemy',damping='0.2',freq='5' ))
    lb.addObject(Joints.DistanceJoint(body1='Beam_left',body2='Spikey',damping='0.2',freq='5' ))
    lb.render()