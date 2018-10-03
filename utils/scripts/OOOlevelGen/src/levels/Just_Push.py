import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=460,y=16))
    
    lb.addObject(Beam.BeamSprite(x=240,y=320,width=10,height=10,static='true',angle=0).setName("Hook"))
    
    distJoint = Joints.DistanceJoint(body1="Star",body2="Hook",damping='10',freq='0')
    lb.addObject(distJoint)
    
    lb.addObject(Star.StarSprite(x=240,y=290,width=32,height=32))
    
    lb.addObject(Enemy.EnemySprite(x=340,y=265,width=100,height=100, restitution=0.8,desity=1))
    lb.addObject(Enemy.EnemySprite(x=240,y=265,width=40,height=40, restitution=0,density=4))
    lb.addObject(Friend.FriendSprite(x=170,y=265,width=100,height=100, restitution=0.0))
    
    lb.addObject(Beam.BeamSprite(x=240,y=200,width=274,height=30,static='true',angle=0).setName("platform"))
    lb.addObject(Beam.BeamSprite(x=240-137,y=200,width=60,height=10,static='true',angle=90))
    
    #lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=280,y=160,width=200,height=200,enemy_size=60))

    lb.render()
