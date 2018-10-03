import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=175,y=40))
    lb.addObject(Star.StarSprite(x=16,y=140,width=32,height=32,static='true'))

    #lb.addObject(Bomb.BombSprite(x=450,y=50,width=32,height=32,static='false'))

    lb.addObject(Enemy.EnemySprite(x=250,y=25,width=50,height=50, density=50, friction=200,static='false').setName("e1"))
    lb.addObject(Enemy.EnemySprite(x=100,y=25,width=50,height=50, density=50, friction=200,static='false').setName("e2"))
    #lb.addObject(Enemy.EnemySprite(x=175,y=30,width=32,height=32, density=1, friction=200,static='false').setName("e3"))
    distJoint = Joints.DistanceJoint(body1="e1",body2="e2",damping='10',freq='0')
    distJoint2 = Joints.DistanceJoint(body1="Hero",body2="e2",damping='10',freq='0')
    distJoint3 = Joints.DistanceJoint(body1="Hero",body2="e1",damping='10',freq='0')
    lb.addObject(distJoint)
    lb.addObject(distJoint2)
    lb.addObject(distJoint3)
    
    #lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=300,width=40,height=40,density=10))
    
    
    lb.addObject(Beam.BeamSprite(x=60,y=200,width=10,height=10,static='true',angle=0).setName("platform"))
    #lb.addObject(Beam.BeamSprite(x=240,y=-125,width=200,height=200,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=480,y=-100,width=200,height=200,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=0,y=-100,width=200,height=200,static='true',angle=45))

    
    distJoint4 = Joints.DistanceJoint(body1="platform",body2="Star",damping='10',freq='0')
    lb.addObject(distJoint4)
     
    #lb.addObject(Contacts.Contact(body1='Spikey',body2='e1',event_name='onDestroy'))
    #lb.addObject(Contacts.Contact(body1='Spikey',body2='e2',event_name='onDestroy'))

    #lb.addObject(Contacts.Contact(body1='Hero',body2='e'+str(e),event_name='onLose'))


    lb.render()
