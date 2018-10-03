import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=65, y=181,width=17,height=17,restitution=0.5,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=215, y=-4,width=126,height=61,angle='22',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Hero.HeroSprite(x=25, y=182,width=32,height=32))	lb.addObject(Launcher.LauncherSprite(name='defaultValue',x=453, y=15, trigger_x=410, trigger_y=231))	lb.addObject(Beam.BeamSprite(x=313, y=9,width=126,height=61,angle='22',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=393, y=26,width=66,height=69,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=439, y=180,width=13,height=168,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=349, y=251,width=13,height=172,angle='-86',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=449, y=314,width=126,height=26,angle='-20',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=264, y=315,width=577,height=26,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=159, y=252,width=13,height=172,angle='86',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Enemy.EnemySprite(x=220, y=271,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Star.StarSprite(x=254, y=267,width=32,height=32))	lb.addObject(Enemy.EnemySprite(x=288, y=271,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=320, y=274,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=357, y=275,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=393, y=280,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=426, y=280,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=185, y=273,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=152, y=277,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=119, y=278,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=86, y=281,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=279, y=44,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Rotor.RotorSprite(x=365,y=173,speed=0,angle=0,torque=100))	lb.addObject(Enemy.EnemySprite(x=325, y=201,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=405, y=201,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=74, y=-4,width=175,height=61,angle='-14',restitution=0.8,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=31, y=287,width=13,height=111,angle='56',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.render()