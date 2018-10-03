import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Hero.HeroSprite(x=111, y=17,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=382, y=17,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=32, y=27,width=52,height=52,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=188, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=446, y=30,width=58,height=58,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=297, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=377, y=72,width=185,height=14,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=109, y=72,width=185,height=14,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=242, y=298,width=32,height=32))
    lb.render()