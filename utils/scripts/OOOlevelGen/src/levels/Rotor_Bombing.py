import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Enemy.EnemySprite(x=244, y=16,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ).setName('Bomb'))
    lb.addObject(Enemy.EnemySprite(x=244, y=54,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=244, y=100,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=244, y=142,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=285, y=100,width=32,height=32))
    lb.addObject(Bomb.BombSprite(x=327, y=16,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=327, y=54,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Friend.FriendSprite(x=327, y=100,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=327, y=142,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=32, y=23,width=32,height=32))
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=108,y=150,scaling=1.6242218017578125,speed=3000,torque=3))
    lb.render()