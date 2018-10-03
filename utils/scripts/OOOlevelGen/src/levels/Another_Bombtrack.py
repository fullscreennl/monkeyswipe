import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=275, y=268,width=502,height=14,angle='3',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Bomb.BombSprite(x=384, y=291,width=20,height=20 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Bomb.BombSprite(x=293, y=285,width=20,height=20 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Bomb.BombSprite(x=315, y=287,width=20,height=20 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Bomb.BombSprite(x=249, y=283,width=20,height=20 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Bomb.BombSprite(x=361, y=290,width=20,height=20 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=412, y=293,width=20,height=20))
    lb.addObject(Enemy.EnemySprite(x=199, y=130,width=246,height=246,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Enemy'))
    lb.addObject(Beam.BeamSprite(x=10, y=313,width=21,height=14,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('BeamHook'))
    lb.addObject(Hero.HeroSprite(x=16, y=120,width=32,height=32))
    lb.addObject(Joints.DistanceJoint(body1='BeamHook',body2='Hero',damping='0.2',freq='5' ))
    lb.addObject(Enemy.EnemySprite(x=338, y=287,width=20,height=20,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=271, y=284,width=20,height=20,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.render()