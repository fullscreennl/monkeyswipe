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

EnemyEquipedRotor: lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=200,y=160,scaling=1.5,speed=10,torque=10000))
CyclingEnemyObject : CyclingEnemyObject.CyclingEnemyObjectSprite(name='num1',x=240,y=160,width=120,height=120,enemy_size=40)

Bomb: lb.addObject(Bomb.BombSprite(x=240,y=200,width=50,height=50,static='true'))

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
	
	lb.addObject(Beam.BeamSprite(x=240,y=190,width=250,height=30,static='true',angle=90))
	
	xpos = 80
	yposbeams = 166 
	yposballs = 16
	beams = [(xpos+96,yposbeams),(xpos+128,yposbeams),(xpos+160,yposbeams),(xpos+192,yposbeams),(xpos+224,yposbeams)]
	friends = [(xpos+96-(yposbeams-yposballs),yposbeams),(xpos+128,yposballs),(xpos+160,yposballs),(xpos+192,yposballs),(xpos+224,yposballs)]
	i=0
	for beam in beams:
		lb.addObject(Beam.BeamSprite(x=beam[0],y=beam[1],width=20,height=20,static='true',angle=0).setName("beam_"+str(i)))
		i = i+1
	i=0
	for friend in friends:
		if i==0 or i==4:
			lb.addObject(Enemy.EnemySprite(x=friend[0],y=friend[1],width=30,height=30,restitution=1,static='false',angle=0).setName("friend_"+str(i)))
		else:	
			lb.addObject(Friend.FriendSprite(x=friend[0],y=friend[1],width=30,height=30,restitution=1,static='false',angle=0).setName("friend_"+str(i)))
		distJoint = Joints.DistanceJoint(body1='beam_'+str(i),body2='friend_'+str(i),damping='0',freq='10')   
		lb.addObject(distJoint)
		i = i+1	
	#lb.addObject(Star.StarSprite(x=280,y=310,width=30,height=30))
	lb.addObject(Beam.BeamSprite(x=40,y=220,width=90,height=20,static='true',angle=0))
	lb.addObject(Hero.HeroSprite(x=40,y=240))
	
	lb.addObject(Beam.BeamSprite(x=0,y=0,width=150,height=150,static='true',angle=45))
	lb.addObject(Beam.BeamSprite(x=480,y=0,width=150,height=150,static='true',angle=45))
    
	lb.addObject(Contacts.Contact(body1='friend_0',body2='Hero',event_name='onLose'))
	lb.addObject(Contacts.Contact(body1='friend_4',body2='Hero',event_name='onLose'))
	#lb.addObject(Enemy.EnemySprite(x=240,y=200,width=320,height=320))
	lb.addObject(EnemyBucketWithStar.EnemyBucketWithStarSprite(width=170,height=80, x=380, y=270, num_enemies=3, enemy_size=30))
	lb.render()
