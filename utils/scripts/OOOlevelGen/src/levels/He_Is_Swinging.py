import LevelBuilder
from sprites import *
def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
    lb.addObject(Beam.BeamSprite(x=384, y=311,width=10,height=10,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Hook'))
    lb.addObject(Enemy.EnemySprite(x=221, y=304,width=32,height=32,angle='0',restitution=1,static='false',friction=0.01,density=5 ).setName('Dangler'))
    lb.addObject(Joints.DistanceJoint(body1='Hook',body2='Dangler',damping='0.01',freq='30' ))
    lb.addObject(Beam.BeamSprite(x=460, y=254,width=39,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.addObject(Star.StarSprite(x=460, y=290,width=32,height=32))
    lb.addObject(Hero.HeroSprite(x=28, y=31,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=425, y=36,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))
    lb.addObject(Contacts.Contact(body1='Hero',body2='Dangler',event_name='onLose'))
    lb.addObject(Beam.BeamSprite(x=384, y=237,width=133,height=14,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))
    lb.render()