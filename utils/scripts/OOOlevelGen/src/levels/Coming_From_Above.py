import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Enemy.EnemySprite(x=196, y=248,width=32,height=32,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=230, y=223,width=15,height=15,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=232, y=263,width=42,height=42,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=268, y=260,width=22,height=22,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=295, y=223,width=27,height=27,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=266, y=181,width=54,height=54,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=372, y=191,width=93,height=93,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=340, y=255,width=12,height=12,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=284, y=301,width=24,height=24,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=135, y=287,width=14,height=14,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=141, y=236,width=16,height=16,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=171, y=196,width=61,height=61,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=122, y=183,width=7,height=7,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=180, y=287,width=50,height=50,angle='0',restitution=0.9,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=46, y=203,width=90,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Hero.HeroSprite(x=61, y=169,width=32,height=32))	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=21, y=171,width=40,height=40,restitution=0.9,static='false',friction=0.5,density=10 ))	lb.addObject(Beam.BeamSprite(x=46, y=143,width=92,height=14,angle='0',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=240, y=7,width=482,height=14,angle='0',restitution=1.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Star.StarSprite(x=462, y=178,width=32,height=32))	lb.render()