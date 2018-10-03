import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=240,y=301))

    lb.addObject(Beam.BeamSprite(x=240,y=280,width=10,height=10,static='true',angle=0).setName("hook"))

    lb.addObject(Enemy.EnemySprite(x=240,y=85,width=20,height=20,density='1'))
    lb.addObject(Enemy.EnemySprite(x=240,y=85,width=20,height=20,density='1'))
    
    lb.addObject(Star.StarSprite(x=240,y=85,width=20,height=20))
    distJoint = Joints.DistanceJoint(body1='hook',body2='Star',damping='10',freq='15')
    lb.addObject(distJoint)
    
    #lb.addObject(Bomb.BombSprite(x=240,y=100,width=32,height=32,static='false'))
    #distJoint = Joints.DistanceJoint(body1='hook',body2='Bomb',damping='10',freq='15')
    #lb.addObject(distJoint)

    for en in range(10):
        lb.addObject(Enemy.EnemySprite(x=240,y=115,width=32,height=32,static='false').setName("en"+str(en)))
        distJoint = Joints.DistanceJoint(body1='hook',body2="en"+str(en),damping='10',freq='15')
        lb.addObject(distJoint)
        lb.addObject(Contacts.Contact(body1='Hero',body2='en'+str(en),event_name='onLose'))
    
    for fn in range(10):
        lb.addObject(Friend.FriendSprite(x=240,y=50,width=32,height=32,static='false',restitution='0.8').setName("fn"+str(fn)))
        distJoint = Joints.DistanceJoint(body1='hook',body2="fn"+str(fn),damping='10',freq='15')
        lb.addObject(distJoint)
    
    lb.render()
