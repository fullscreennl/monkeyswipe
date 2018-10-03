import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Friend.FriendSprite(x=227, y=148,width=100,height=100,angle='0',restitution=0.2,static='false',friction=0.9,density=1 ).setName('Friend3'))	lb.addObject(Hero.HeroSprite(x=62, y=18,width=32,height=32))	lb.addObject(Friend.FriendSprite(x=165, y=50,width=100,height=100,angle='0',restitution=0.2,static='false',friction=0.9,density=10 ).setName('Friend2'))	lb.addObject(Friend.FriendSprite(x=290, y=50,width=100,height=100,angle='0',restitution=0.2,static='false',friction=0.9,density=10 ).setName('Friend1'))	lb.addObject(Enemy.EnemySprite(x=227, y=148,width=130,height=130,angle='0',restitution=0.2,static='false',friction=0.8,density=2 ).setName('Enemy'))	lb.addObject(Joints.DistanceJoint(body1='Friend3',body2='Friend1',damping='0.2',freq='.2' ))	lb.addObject(Joints.DistanceJoint(body1='Friend3',body2='Friend2',damping='0.2',freq='.2' ))	lb.addObject(Star.StarSprite(x=228, y=17,width=32,height=32))	lb.addObject(Joints.DistanceJoint(body1='Friend3',body2='Enemy',damping='0.2',freq='10' ))	lb.addObject(Joints.RevoluteJoint(body1='Friend3',body2='Friend4',motor_speed='2000',enable_motor='true',torque='10000',lower_angle='12',upper_angle='50',enable_limit='false',collide_connected='false'))	lb.addObject(Friend.FriendSprite(x=226, y=222,width=16,height=16,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend4'))	lb.render()