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

	lb.addObject(Hero.HeroSprite(x=16,y=16))
	lb.addObject(Beam.BeamSprite(x=50,y=16,width=32,height=32,static='false',angle=0).setName("blockie"))
	distJoint = Joints.DistanceJoint(body1='Hero',body2='blockie',damping='0.2',freq='0.8')   
	lb.addObject(distJoint)
	#lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=240,y=160,width=32,height=32,density='1',restitution='0.7'))
	
	#static beams
	lb.addObject(Star.StarSprite(x=180,y=305,width=30,height=30))
	nuts = [(385,50),(385,280),(412,50)]
	for nut in nuts:
		lb.addObject(Nut.NutSprite(x=nut[0],y=nut[1]))
	lb.addObject(Beam.BeamSprite(x=400,y=180,width=277,height=15,static='false',angle=90))
	lb.addObject(Beam.BeamSprite(x=190,y=250,width=350,height=15,static='true',angle=0))
	lb.addObject(Beam.BeamSprite(x=240,y=3,width=480,height=50,static='true',angle=0)) #groundlbock
	#lb.addObject(Beam.BeamSprite(x=450,y=220,width=350,height=15,static='false',angle=0))
	enemies = [(450,220,30),(450,300,30),(450,300,30),(460,250,30),(450,250,30),(450,220,30),(450,250,30),(450,250,30),(450,120,30),(450,120,30),(450,90,30),(450,120,30),(450,80,30),(450,140,30),(450,190,30),(450,120,30),(450,120,30),(450,120,30),(450,300,30),(450,300,30),(450,300,30),(450,300,30)]
	for enemy in enemies:
		lb.addObject(Enemy.EnemySprite(x=enemy[0], y=enemy[1], width=enemy[2], height=enemy[2]))

	lb.addObject(Enemy.EnemySprite(x=200, y=75, width=150, height=150))	
	lb.render()
