import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=240,y=40))
    lb.addObject(Star.StarSprite(x=80,y=150,width=32,height=32))
    
    lb.addObject(Beam.BeamSprite(x=240,y=160,width=10,height=10,static='true',angle=0).setName("platform"))
    
    
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=240,y=250,scaling=1.0,speed=3,torque=10000))
    
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=60,y=160,width=80,height=80,enemy_size=20))
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num2',x=420,y=160,width=80,height=80,enemy_size=20))

    
    distJoint = Joints.DistanceJoint(body1="Hero",body2="platform",damping='10',freq='0')
    lb.addObject(distJoint)

    lb.addObject(Friend.FriendSprite(x=300,y=125,width=64,height=64,denstity=0.02))
    
    lb.addObject(Beam.BeamSprite(x=480,y=-100,width=200,height=200,static='true',angle=45))
    lb.addObject(Beam.BeamSprite(x=0,y=-100,width=240,height=240,static='true',angle=60))

    lb.render()
