import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=450,y=16))
    lb.addObject(Star.StarSprite(x=100,y=16,width=32,height=32))

    lb.addObject(Beam.BeamSprite(x=240-50,y=10,width=20,height=20,static='true',angle=0,density=2).setName('base1'))
    lb.addObject(Beam.BeamSprite(x=240+50,y=10,width=20,height=20,static='true',angle=0,density=2).setName('base2'))
 
    lb.addObject(Enemy.EnemySprite(x=240,y=125,width=128,height=128,density=1).setName("Enemy1"))
    lb.addObject(Contacts.Contact(body1='Hero',body2='Enemy1',event_name='onLose'))
 
    distJoint = Joints.DistanceJoint(body1='base1',body2='Enemy1',damping='0.1',freq='0.6')   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='base2',body2='Enemy1',damping='0.1',freq='0.6')   
    lb.addObject(distJoint)
    
    lb.addObject(Beam.BeamSprite(x=300-50,y=10,width=20,height=20,static='true',angle=0,density=2).setName('base3'))
    lb.addObject(Beam.BeamSprite(x=300+50,y=10,width=20,height=20,static='true',angle=0,density=2).setName('base4'))
 
    #lb.addObject(Friend.FriendSprite(x=300,y=280,width=60,height=60,density=1).setName('Friend2'))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=300,y=280,width=40,height=40,density=1,restitution=0.6))
 
    distJoint = Joints.DistanceJoint(body1='base3',body2='Spikey',damping='0.1',freq='3')   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='base4',body2='Spikey',damping='0.1',freq='3')   
    lb.addObject(distJoint)
    
    lb.addObject(Beam.BeamSprite(x=100-50,y=10,width=20,height=20,static='true',angle=0,density=2).setName('base5'))
    lb.addObject(Beam.BeamSprite(x=100+50,y=10,width=20,height=20,static='true',angle=0,density=2).setName('base6'))
 
    lb.addObject(Enemy.EnemySprite(x=100,y=90,width=128,height=128,density=1).setName("Enemy"))
 
    distJoint = Joints.DistanceJoint(body1='base5',body2='Enemy',damping='0.1',freq='1')   
    lb.addObject(distJoint)
    distJoint = Joints.DistanceJoint(body1='base6',body2='Enemy',damping='0.1',freq='1')   
    lb.addObject(distJoint)
    
    #lb.addObject(Bomb.BombSprite(x=200,y=16,width=32,height=32,static='false'))
    
    
    
    #lb.addObject(Contacts.Contact(body1='Hero',body2=':hat_top',event_name='onRemoteExplode'))
    
    lb.render()