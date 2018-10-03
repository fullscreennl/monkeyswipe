import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Launcher.LauncherSprite(name='launcher',x=26, y=15, trigger_x=154, trigger_y=72))
    lb.addObject(Beam.BeamSprite(x=116, y=53,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=10, y=311,width=127,height=25,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=173, y=114,width=127,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=227, y=195,width=251,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=284, y=74,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=250, y=97,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=122, y=203,width=127,height=14,angle='-30',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=27, y=81,width=35,height=35,restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Hero.HeroSprite(x=250, y=35,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=316, y=34,width=59,height=59,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=347,y=175,scaling=1.4296875,speed=-1,torque=500))
    lb.addObject(Beam.BeamSprite(x=346, y=332,width=127,height=14,angle='-90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()