import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Hero.HeroSprite(x=240, y=238,width=32,height=32))	lb.addObject(Beam.BeamSprite(x=240, y=213,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Friend.FriendSprite(x=196, y=230,width=18,height=18,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend2'))	lb.addObject(Friend.FriendSprite(x=284, y=230,width=18,height=18,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Friend1'))	lb.addObject(Enemy.EnemySprite(x=320, y=213,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Enemy1'))	lb.addObject(Enemy.EnemySprite(x=160, y=214,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Enemy4'))	lb.addObject(Enemy.EnemySprite(x=160, y=177,width=16,height=16,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Enemy5'))	lb.addObject(Enemy.EnemySprite(x=160, y=151,width=16,height=16,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Enemy6'))	lb.addObject(Enemy.EnemySprite(x=320, y=179,width=16,height=16,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Enemy2'))	lb.addObject(Enemy.EnemySprite(x=320, y=152,width=16,height=16,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Enemy3'))	lb.addObject(Joints.DistanceJoint(body1='Hero',body2='Friend1',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Enemy1',body2='Friend1',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Enemy1',body2='Enemy2',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Enemy3',body2='Enemy2',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Hero',body2='Friend2',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Enemy4',body2='Friend2',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Enemy4',body2='Enemy5',damping='0.2',freq='5' ))	lb.addObject(Joints.DistanceJoint(body1='Enemy5',body2='Enemy6',damping='0.2',freq='5' ))	lb.addObject(Star.StarSprite(x=238, y=94,width=32,height=32))	lb.addObject(Nut.NutSprite(x=240, y=202,width=13,height=13,eventName='onNutHit' ,restitution=0.2,static='true',friction=0.5,density=20 ).setName('Nut'))	lb.addObject(Joints.DistanceJoint(body1='Nut',body2='Star',damping='0.2',freq='5' ))	lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy1',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy2',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy3',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy4',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy5',event_name='onLose'))	lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy6',event_name='onLose'))	lb.render()