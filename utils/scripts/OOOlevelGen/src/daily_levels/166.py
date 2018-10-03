import LevelBuilder
from sprites import *

def render(name,bg):
    lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)

    lb.addObject(Hero.HeroSprite(x=305, y=16,width=32,height=32))
    lb.addObject(Enemy.EnemySprite(x=352, y=88,width=54,height=54,static='false',angle='0'))
    lb.addObject(Star.StarSprite(x=16, y=17,width=32,height=32))
    lb.addObject(Beam.BeamSprite(x=90, y=62,width=164,height=41,static='true',angle='105'))
    lb.addObject(CyclingEnemyObject.CyclingEnemyObjectSprite(name='cycle_1',x=78,y=249,width=60,height=60,enemy_size=20))
    lb.addObject(EnemyEquipedRotor.EnemyEquipedRotorSprite(x=199,y=82,scaling=1,speed=3000,torque=3))
    lb.addObject(Launcher.LauncherSprite(name='trigger_4',x=354, y=15, trigger_x=428, trigger_y=280))
    lb.addObject(Wizard.WizardSprite(x=445,y=69))

    
    lb.render()
