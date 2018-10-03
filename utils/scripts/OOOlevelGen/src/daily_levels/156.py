import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    
    lb.addObject(Star.StarSprite(x=240,y=250,width=20,height=20))
    lb.addObject(Enemy.EnemySprite(x=280,y=250,width=20,height=20))
    lb.addObject(Enemy.EnemySprite(x=200,y=250,width=20,height=20))

    #lb.addObject(Friend.FriendSprite(x=240,y=320,width=20,height=20,density=100, friction=200,static='true').setName("hook"))
    
    lb.addObject(Beam.BeamSprite(x=10,y=200,width=20,height=15,static='true',angle=0).setName("filler"))
    lb.addObject(Beam.BeamSprite(x=25,y=200,width=15,height=15,static='true',angle=0).setName("pole_left"))
    lb.addObject(Beam.BeamSprite(x=443,y=200,width=15,height=35,static='true',angle=20).setName("pole_right"))

    #lb.addObject(Bomb.BombSprite(x=180,y=16,width=32,height=32,static='false'))

    prevbody = "pole_left"
    types = [0,0,0,0,1,1,0,0,2,0]
    e = 0
    for t in types:
        if t == 0:
            lb.addObject(Enemy.EnemySprite(x=50 + (e*40),y=180,width=32,height=32, density=1, friction=200,static='false').setName("e"+str(e)))
            lb.addObject(Contacts.Contact(body1='Hero',body2='e'+str(e),event_name='onLose'))
            currentbody = "e"+str(e)
        elif t == 1:
            lb.addObject(Friend.FriendSprite(x=50 + (e*40),y=180,width=40,height=40, density=1, friction=200,static='false').setName("e"+str(e)))
            currentbody = "e"+str(e)
        else:
            lb.addObject(Hero.HeroSprite(x=50+(e*40),y=180))
            currentbody = "Hero"
        distJoint = Joints.DistanceJoint(body1=prevbody,body2=currentbody,damping='10',freq='15')
        prevbody = currentbody
        lb.addObject(distJoint)
        e = e+1
        
    #lb.addObject(Beam.BeamSprite(x=200,y=0,width=50,height=50,static='true',angle=45))
    #lb.addObject(Friend.FriendSprite(x=400,y=20,width=40,height=40, density=1, friction=10,static='false'))

    distJoint = Joints.DistanceJoint(body1=prevbody,body2="pole_right",damping='10',freq='15')
    lb.addObject(distJoint)

    lb.render()
