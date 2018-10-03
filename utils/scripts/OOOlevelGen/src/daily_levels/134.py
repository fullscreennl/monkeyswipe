import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=300,y=40))
    lb.addObject(Beam.BeamSprite(x=300,y=160,width=10,height=10,static='true',angle=0).setName("platform"))
    distJoint = Joints.DistanceJoint(body1="Hero",body2="platform",damping='10',freq='0')
    lb.addObject(distJoint)
    
    lb.addObject(Star.StarSprite(x=140,y=40,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=140,y=160,width=10,height=10,static='true',angle=0).setName("platform2"))
    distJoint = Joints.DistanceJoint(body1="Star",body2="platform2",damping='10',freq='0')
    lb.addObject(distJoint)
    
    lb.addObject(Enemy.EnemySprite(x=400,y=40,width=32,height=32,denstity=0.02))
    lb.addObject(Beam.BeamSprite(x=400,y=160,width=10,height=10,static='true',angle=0).setName("platform3"))
    distJoint = Joints.DistanceJoint(body1="Enemy",body2="platform3",damping='10',freq='0')
    lb.addObject(distJoint)

    #lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=240,y=250,scaling=1.0,speed=3,torque=10000))
    
    #lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=60,y=160,width=80,height=80,enemy_size=20))
    #lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num2',x=420,y=160,width=80,height=80,enemy_size=20))
    
   

    lb.addObject(Friend.FriendSprite(x=300,y=125,width=64,height=64,denstity=0.02))
    #lb.addObject(Enemy.EnemySprite(x=100,y=125,width=64,height=64,denstity=0.02))
    
    lb.addObject(Beam.BeamSprite(x=480,y=-100,width=200,height=200,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=0,y=-100,width=240,height=240,static='true',angle=60))

    lb.render()
