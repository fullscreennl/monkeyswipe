import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Enemy.EnemySprite(x=240, y=245,width=133,height=133,angle='0',restitution=1,static='false',friction=0.5,density=20 ).setName('Enemy'))	lb.addObject(Hero.HeroSprite(x=41, y=24,width=32,height=32))	lb.addObject(Star.StarSprite(x=460, y=200,width=32,height=32))	lb.addObject(Nut.NutSprite(x=400, y=301,width=13,height=13,eventName='onNutHit' ,restitution=0.2,static='true',friction=0.5,density=20 ).setName('Nut'))	lb.addObject(Joints.DistanceJoint(body1='Nut',body2='Star',damping='0',freq='15' ))	lb.render()