import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Bomb.BombSprite(x=194, y=16,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ).setName('Bomb_left'))
    lb.addObject(Bomb.BombSprite(x=302, y=16,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ).setName('Bomb_right'))
    lb.addObject(Beam.BeamSprite(x=249, y=41,width=143,height=14,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=249, y=163,width=228,height=228,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=249, y=163,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=19, y=20,width=32,height=32))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=460, y=20,width=40,height=40,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Joints.RevoluteJoint(body1='Enemy',body2='Star',motor_speed='50',enable_motor='true',torque='1000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))
    lb.addObject(Contacts.Contact(body1='Hero',body2='Bomb_right',event_name='onSimpleExplode'))
    lb.addObject(Contacts.Contact(body1='Hero',body2='Bomb_left',event_name='onSimpleExplode'))
    lb.render()
