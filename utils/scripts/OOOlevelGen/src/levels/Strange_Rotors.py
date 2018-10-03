import LevelBuilder
from sprites import *

"""
### Creating builder ###

level:    lb = LevelBuilder.LevelBuilder("level_34.plist")

### Adding sprites ###

Hero:     lb.addObject(Hero.HeroSprite(x=20,y=10))

Rotor:    lb.addObject(Rotor.RotorSprite(x=180,y=110,speed=5,torque=10000))

Bucket:   lb.addObject(EnemyBucketWithStar.EnemyBucketWithStarSprite(width=100,height=75, x=240, y=160, num_enemies=10, enemy_size=20))

Launcher: lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=260, y=50, trigger_x=400, trigger_y=100))

Beam:     lb.addObject(Beam.BeamSprite(x=240+40,y=25,width=30,height=60,static='true',angle=0))

Nut:      lb.addObject(Nut.NutSprite(x=50,y=200))

Enemy:    lb.addObject(Enemy.EnemySprite(x=240,y=200,width=50,height=50))

Friend:   lb.addObject(Friend.FriendSprite(x=240,y=125,width=128,height=128))

Wizard:   lb.addObject(Wizard.WizardSprite(x=25,y=50))

Spikey:   lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=50,y=80,width=50,height=50))

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
	#lb.addObject(Beam.BeamSprite(x=32,y=16,width=35,height=15,static='false',angle=0, density=1).setName("Balkje"))	lb.addObject(Rotor.RotorSprite(x=60,y=260,speed=-5,angle=0,torque=1000))	lb.addObject(Hero.HeroSprite(x=20, y=18,width=32,height=32))	lb.addObject(Star.StarSprite(x=462, y=300,width=32,height=32))	lb.addObject(Enemy.EnemySprite(x=431, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Rotor.RotorSprite(x=260,y=60,speed=-5,angle=0,torque=1000))	lb.addObject(Rotor.RotorSprite(x=210,y=110,speed=5,angle=-45,torque=1000))	lb.addObject(Rotor.RotorSprite(x=110,y=210,speed=5,angle=-45,torque=1000))	lb.addObject(Rotor.RotorSprite(x=160,y=160,speed=-5,angle=0,torque=1000))	lb.addObject(Beam.BeamSprite(x=360, y=275,width=246,height=14,static='true',angle='1'))	lb.addObject(Enemy.EnemySprite(x=419, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=407, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=395, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=384, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=372, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=360, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=349, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=337, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=314, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=325, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=302, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=290, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=278, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=267, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=255, y=288,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Nut.NutSprite(x=438, y=311,width=15,height=15,static='true'))	lb.addObject(Enemy.EnemySprite(x=437, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=425, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=414, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=402, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=390, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=379, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=367, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=355, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=343, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=320, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=332, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=308, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=297, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=285, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=273, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.addObject(Enemy.EnemySprite(x=262, y=297,width=8,height=8,density='3',static='false',angle='0'))	lb.render()
