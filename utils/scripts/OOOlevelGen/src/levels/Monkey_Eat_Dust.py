import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Beam.BeamSprite(x=7, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=45, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=38, y=41,width=27,height=4,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=18, y=41,width=27,height=4,angle='-30',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=79, y=33,width=27,height=4,angle='135',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=79, y=13,width=27,height=4,angle='60',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=61, y=11,width=27,height=4,angle='-45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=61, y=31,width=27,height=4,angle='-120',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=95, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=111, y=25,width=54,height=4,angle='-60',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=127, y=25,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=137, y=25,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=149, y=14,width=27,height=4,angle='-45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=149, y=34,width=27,height=4,angle='-120',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=206, y=14,width=29,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=164, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=177, y=45,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=177, y=5,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=177, y=24,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=215, y=33,width=27,height=4,angle='45',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=195, y=33,width=27,height=4,angle='-30',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=363, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=376, y=36,width=27,height=4,angle='135',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=376, y=16,width=27,height=4,angle='60',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=393, y=24,width=46,height=4,angle='105',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=246, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=259, y=45,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=259, y=5,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=259, y=24,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=421, y=24,width=46,height=4,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=435, y=23,width=27,height=4,angle='135',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=439, y=7,width=16,height=4,angle='60',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=432, y=38,width=16,height=4,angle='60',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=409, y=3,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=303, y=25,width=54,height=4,angle='-75',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=288, y=25,width=54,height=4,angle='-105',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=295, y=17,width=27,height=4,angle='-180',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=322, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=322, y=50,width=36,height=4,angle='-165',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=460, y=24,width=46,height=4,angle='90',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Beam.BeamSprite(x=460, y=50,width=36,height=4,angle='-165',restitution=0.2,static='true',friction=0.5,density=20 ).setName('Beam'))	lb.addObject(Enemy.EnemySprite(x=414, y=64,width=32,height=32,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=317, y=61,width=21,height=21,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=196, y=61,width=21,height=21,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Enemy.EnemySprite(x=71, y=22,width=18,height=18,angle='0',restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=368, y=85,width=164,height=7,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=151, y=98,width=164,height=7,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=279, y=159,width=164,height=7,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=162, y=220,width=164,height=7,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=387, y=271,width=164,height=7,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Star.StarSprite(x=408, y=14,width=16,height=16))	lb.addObject(Hero.HeroSprite(x=104, y=251,width=32,height=32))	lb.addObject(Beam.BeamSprite(x=310, y=122,width=64,height=6,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=205, y=128,width=50,height=6,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=223, y=189,width=50,height=6,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=337, y=215,width=100,height=6,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=99, y=159,width=113,height=6,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=440, y=177,width=176,height=6,angle='90' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=273, y=178,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=305, y=178,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=294, y=205,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=262, y=214,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=282, y=237,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=254, y=251,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=226, y=242,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=282, y=264,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=254, y=275,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=310, y=231,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=243, y=190,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=230, y=133,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=290, y=137,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=289, y=107,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=318, y=205,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.addObject(Beam.BeamSprite(x=98, y=74,width=21,height=20,angle='0' ,restitution=0.2,static='false',friction=0.5,density=20 ))	lb.render()