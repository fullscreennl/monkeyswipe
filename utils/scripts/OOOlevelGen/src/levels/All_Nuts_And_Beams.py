import LevelBuilder
from sprites import *

"""
### Creating builder ###

level:    lb = LevelBuilder.LevelBuilder("level_34.plist")

### Adding sprites ###

Hero:     lb.addObject(Hero.HeroSprite(x=20,y=10))

Rotor:    lb.addObject(Rotor.RotorSprite(x=180,y=110,speed=5,torque=10000))

Bucket:   lb.addObject(EnemyBucketWithStar.EnemyBucketWithStarSprite(width=100,height=75, x=240, y=160, num_enemies=10, enemy_size=20))

Launcher: lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=260, y=50, trigger_x=400, trigger_y=100,power='#20000'))

Beam:     lb.addObject(Beam.BeamSprite(x=240+40,y=25,width=30,height=60,static='true',angle=0))

Nut:      lb.addObject(Nut.NutSprite(x=50,y=200))

Enemy:    lb.addObject(Enemy.EnemySprite(x=240,y=200,width=50,height=50))

Friend:   lb.addObject(Friend.FriendSprite(x=240,y=125,width=128,height=128))

Wizard:   lb.addObject(Wizard.WizardSprite(x=25,y=50))

Spikey:   lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=50,y=80,width=50,height=50))

EnemyEquipedRotor: lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=160,y=240,speed=2,torque=10000))
CyclingEnemyObject : CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=240,y=160,width=120,height=120,enemy_size=40)

### Custom names ###

Setting custom Name (for joints and Contact defs): Hero.HeroSprite(x=20,y=10).setName("piet")


### Adding Joints ###

RevJoint:   revJoint = Joints.RevoluteJoint(body1='body_1',body2='body_2',motor_speed='50.0',torque='1000.0',enable_motor='true',lower_angle='12',upper_angle='45',enable_limit='false',collide_connected='false')
            lb.addObject(revJoint)
          
PrismJoint: prismJoint = Joints.PrismaticJoint(body1='body_1',motor_speed='50.0',torque='1000.0',enable_motor='true',lower_translation='-100',upper_translation='100',enable_limit='false',vertical=False)
            lb.addObject(prismJoint)
            
DistJoint:  distJoint = Joints.DistanceJoint(body1='body_1',body2='body_2',damping='0.2',freq='0.8')   
            lb.addObject(distJoint)
            
### Adding Contacts ###

Contact: Contacts.Contact(body1='test',body2='test2',event_name='onTest')
            
lb.render()

"""

def render(name,bg):
	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)
	lb.addObject(Hero.HeroSprite(x=80,y=30))
	lb.addObject(Star.StarSprite(x=370,y=305,width=30,height=30))
	allnuts = [(155,75),(175,75),(235,75),(225,135),(245,135),(270,135),(260,195),(280,195),
	(340,195),(330,255),(350,255),(400,255),(390,310),(410,310),(25,75),(50,75),(70,90),(70,135),(150,135),(170,160),(170,235),(230,235),(250,255),(250,300)]
	for nut in allnuts:
		lb.addObject(Nut.NutSprite(x=nut[0],y=nut[1]))
	lb.addObject(Beam.BeamSprite(x=160,y=60,width=50,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=200,y=85,width=90,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=235,y=110,width=51,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=247,y=140,width=60,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=270,y=170,width=51,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=305,y=200,width=95,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=340,y=230,width=51,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=370,y=260,width=61,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=400,y=300,width=51,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=30,y=80,width=65,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=60,y=110,width=50,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=110,y=140,width=110,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=160,y=190,width=90,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=210,y=240,width=85,height=10,static='false',angle=0))
	lb.addObject(Beam.BeamSprite(x=240,y=290,width=70,height=10,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=240,y=3,width=480,height=50,static='true',angle=0)) #groundblock
	
	allenemies = [(40,300,30),(450,60,120),(450,300,30),(460,250,30),(220,300,60),(40,300,120),(200,300,30),(120,300,30),(30,300,30),(30,300,30),(30,300,30),(30,300,30),
	(30,300,30),(30,300,30),(30,300,30),(20,200,30),(20,200,30),(20,200,30),(20,200,30),(20,200,30),(20,200,30),(450,300,30),(350,160,30),(450,90,40),(450,60,50),(450,60,50)
	,(450,60,50),(450,60,50),(450,60,30),(450,60,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30),(410,160,30)]
	
	for enemy in allenemies:
		lb.addObject(Enemy.EnemySprite(x=enemy[0],y=enemy[1],width=enemy[2],height=enemy[2]))
	#lb.addObject(Enemy.EnemySprite(x=240,y=200,width=320,height=320))
	lb.render()
