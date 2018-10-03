import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Launcher.LauncherSprite(name='launcher_1',x=452, y=87, trigger_x=141, trigger_y=130, power='#2000'))	lb.addObject(Beam.BeamSprite(x=310, y=141,width=222,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=-52, y=143,width=317,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Enemy.EnemySprite(x=459, y=152,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=340, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=303, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=267, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=230, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Hero.HeroSprite(x=451, y=22,width=32,height=32))	lb.addObject(Beam.BeamSprite(x=461, y=277,width=217,height=143,angle='-45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=329, y=269,width=260,height=143,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Enemy.EnemySprite(x=376, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=413, y=167,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Rotor.RotorSprite(x=123,y=203,speed=0,angle=0,torque=1))	lb.addObject(Star.StarSprite(x=88, y=168,width=32,height=32))	lb.render()