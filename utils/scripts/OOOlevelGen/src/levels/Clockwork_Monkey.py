import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=240,y=80))
    lb.addObject(Star.StarSprite(x=240,y=280,width=32,height=32))

    lb.addObject(Friend.FriendSprite(x=240,y=320,width=20,height=20,density=100, friction=200,static='true').setName("hook"))

    #lb.addObject(Bomb.BombSprite(x=180,y=16,width=32,height=32,static='false'))

    prevbody = "hook"
    ypos = 0
    xpos = 0
    enemies = [
               (240 ,240),
               (240 ,200),
               (240 ,160),
               (240 ,120)
               ];
    e = 0;
    
    distJoint = Joints.DistanceJoint(body1=prevbody,body2='Star',damping='10',freq='15')
    lb.addObject(distJoint)
    
    prevbody = 'Star'
    
    for p in enemies:
        e = e + 1
        ypos = p[1]
        xpos = p[0]
        
        lb.addObject(Enemy.EnemySprite(x=xpos,y=ypos,width=32,height=32, density=1, friction=200,static='false').setName("e"+str(e)))
        lb.addObject(Contacts.Contact(body1='Hero',body2='e'+str(e),event_name='onLose'))
        currentbody = "e"+str(e)
        distJoint = Joints.DistanceJoint(body1=prevbody,body2=currentbody,damping='10',freq='15')
        lb.addObject(distJoint)
        prevbody = currentbody
        
    distJoint = Joints.DistanceJoint(body1=prevbody,body2='Hero',damping='10',freq='15')
    lb.addObject(distJoint)
        
    
        


    lb.render()
