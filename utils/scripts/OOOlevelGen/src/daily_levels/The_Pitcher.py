import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='cycler',x=239,y=160,width=206,height=206,enemy_size=32))
    lb.addObject(Enemy.EnemySprite(x=240, y=29,width=53,height=53,angle='0',restitution=0.2,static='false',friction=0.5,density=1 ).setName('Enemy'))
    lb.addObject(Hero.HeroSprite(x=31, y=24,width=32,height=32))
    lb.addObject(Star.StarSprite(x=464, y=236,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=417, y=266,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Beam.BeamSprite(x=458, y=213,width=127,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Enemy.EnemySprite(x=355, y=290,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Beam.BeamSprite(x=58, y=284,width=17,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Hook'))
    lb.addObject(Enemy.EnemySprite(x=135, y=220,width=32,height=32,angle='0',restitution=0.7,static='false',friction=0.5,density=20 ).setName('Dangler'))
    lb.addObject(Joints.DistanceJoint(body1='Hook',body2='Dangler',damping='0.2',freq='5' ))
    lb.addObject(Contacts.Contact(body1='Hero',body2='Dangler',event_name='onLose'))
    lb.render()