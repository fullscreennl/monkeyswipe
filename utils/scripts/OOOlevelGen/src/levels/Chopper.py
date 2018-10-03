import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=40,y=40))
    lb.addObject(Star.StarSprite(x=450,y=150,width=32,height=32))

    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=240,y=168,scaling=1.5,speed=-3,torque=10000,enable_motor="true"))
    lb.addObject(Friend.FriendSprite(x=240,y=328,width=120,height=120,restitution=0.8,static='true',angle=180))
    lb.addObject(Friend.FriendSprite(x=240,y=8,width=120,height=120,restitution=0.8,static='true'))

    lb.render()
