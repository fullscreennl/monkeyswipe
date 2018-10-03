import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Launcher.LauncherSprite(name='launcher_1',x=227, y=15, trigger_x=452, trigger_y=290))
    lb.addObject(Beam.BeamSprite(x=194, y=63,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=260, y=63,width=127,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=227, y=76,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=227, y=133,width=80,height=14,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=227, y=174,width=66,height=66,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=413, y=65,width=124,height=124,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=40, y=27,width=32,height=32))
    lb.render()