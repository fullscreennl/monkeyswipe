import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Beam.BeamSprite(x=249, y=219,width=126,height=4,angle='95',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=231, y=219,width=126,height=4,angle='-95',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=240, y=151,width=44,height=7,angle='0',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=265, y=120,width=53,height=14,angle='-75',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=215, y=120,width=53,height=14,angle='75',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=240, y=84,width=82,height=17,angle='0',restitution=0.2,static='true',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=304, y=40,width=82,height=17,angle='120',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=176, y=40,width=82,height=17,angle='-120',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=240, y=287,width=15,height=7,angle='0',restitution=0.2,static='false',friction=0.9,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=240, y=299,width=15,height=3,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Star.StarSprite(x=240, y=109,width=32,height=32))	lb.addObject(Enemy.EnemySprite(x=240, y=166,width=20,height=20,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=240, y=185,width=17,height=17,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=240, y=201,width=15,height=15,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=240, y=215,width=12,height=12,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=240, y=226,width=11,height=11,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=240, y=236,width=8,height=8,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=240, y=244,width=7,height=7,angle='0',restitution=0.2,static='false',friction=0.5,density=5 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=133, y=17,width=32,height=32,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Enemy'))	lb.addObject(Enemy.EnemySprite(x=347, y=17,width=32,height=32,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Enemy'))	lb.addObject(Hero.HeroSprite(x=27, y=16,width=32,height=32))	lb.render()