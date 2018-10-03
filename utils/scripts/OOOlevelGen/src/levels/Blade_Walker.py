import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=239,y=161,scaling=2.482940673828125,speed=-1,torque=500))
    lb.addObject(Hero.HeroSprite(x=22, y=25,width=32,height=32))
    lb.addObject(Star.StarSprite(x=452, y=31,width=32,height=32))
    lb.render()