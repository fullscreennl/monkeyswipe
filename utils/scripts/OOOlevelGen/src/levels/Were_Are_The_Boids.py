import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=231, y=21,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=287, y=21,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=343, y=21,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=400, y=21,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=455, y=21,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Star.StarSprite(x=373, y=17,width=32,height=32))
    lb.addObject(Bomb.BombSprite(x=431, y=18,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=286, y=68,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=258, y=17,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=315, y=17,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=315, y=47,width=56,height=8,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=371, y=47,width=56,height=8,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=428, y=47,width=56,height=8,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=258, y=47,width=56,height=8,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=372, y=88,width=216,height=8,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=342, y=68,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Enemy.EnemySprite(x=398, y=68,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=287, y=113,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=343, y=113,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=400, y=113,width=43,height=8,angle='-90' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Bomb.BombSprite(x=314, y=109,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Bomb.BombSprite(x=369, y=109,width=32,height=32 ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=343, y=140,width=118,height=8,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Wizard.WizardSprite(x=344,y=212))
    lb.addObject(Friend.FriendSprite(x=454, y=109,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=118,y=107,scaling=1,speed=10,torque=1000))
    lb.addObject(Hero.HeroSprite(x=63, y=270,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=63, y=246,width=38,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Contacts.Contact(body1='Hero',body2=':hat_top',event_name='onRemoteExplode'))
    lb.render()