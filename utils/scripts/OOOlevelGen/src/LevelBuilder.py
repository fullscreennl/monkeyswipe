import os
import config
from sprites import *
import traceback


LEVEL = """

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>level</key>
    <dict>
        <key>name</key>
        <string>level 1 test level</string>
        <key>background</key>
        <string>%(background)s</string>

        <!-- SPRITES -->

        <key>compounds</key>
        <array>
            %(sprites)s
        </array>

        <!-- JOINTS -->

        <key>joints</key>
        <array>
            %(joints)s
        </array>

        <!-- CONTACTS -->

        <key>contacts</key>
        <array>
            %(contacts)s
        </array>
        <!-- SHEETS -->

        <key>sheets</key>
        <array>
            %(sheets)s
        </array>

    </dict>
</dict>
</plist>
"""

SHEETS = """
            <dict>
                <key>atlas</key>
                <string>test_texture</string>
                <key>atlas2</key>
                <string>tut_textures</string>
                <key>id</key>
                <integer>5</integer>
            </dict>
"""

class LevelBuilder:
    def __init__(self,filename,background='doodle_bg.png'):
        self.background = background
        self.filename = filename
        self.object_id = 0
        self.objects = [];
        self.sprites = ""
        self.joints = ""
        self.contacts = ""
        self.contact_filter = {}

    def build(self):
        for obj in self.objects:
            xml = obj.render()
            self.sprites += xml[0]
            self.joints += xml[1]
            try:
                self.contact_filter[xml[2]]
            except:
                self.contacts += xml[2]
                self.contact_filter[xml[2]] = True

    def addJointXML(self,xml):
        self.joints += xml
        
    def addContactXML(self,xml):
        self.contacts += xml
        
    def next(self):
        self.object_id += 1
        return self.object_id

    def addObject(self,obj):
        self.objects.append(obj)

    def render(self):
        self.build()
        xml =  LEVEL%{'background':self.background,'sprites':self.sprites,'joints':self.joints,'sheets':SHEETS,'contacts':self.contacts}
        #print xml
        f = open(config.EXPORT_PATH+self.filename,'w')
        f.write(xml)
        f.close()
        if config.USE_BINARY_PLIST:
            self.convert(config.EXPORT_PATH+self.filename)
        
    def convert(self,file):
        command = "/usr/bin/plutil -convert binary1 "+config.EXPORT_PATH+self.filename
        try:
            #print command
            plutil = os.popen(command, "r")
            #print plutil.readlines()
            status = plutil.close()
            if status:
                raise IOError("plist conversion failed (status %d)" % status)
        except:
            traceback.print_exc(file=self)
            
    def write(self,msg):
        print msg




if __name__ == "__main__":
    lb = LevelBuilder("level_36.plist")
    lb.addObject(Rotor.RotorSprite(x=180,y=110,speed=5,torque=10000))
    #lb.addObject(Rotor.RotorSprite(x=100,y=60,speed=5,torque=10000))
    #lb.addObject(Rotor.RotorSprite(x=300,y=200,speed=20,torque=10000))
    lb.addObject(Hero.HeroSprite(x=20,y=10))
    lb.addObject(Launcher.LauncherSprite(name='__launcher__1',x=260, y=50, trigger_x=400, trigger_y=100))
    lb.addObject(Launcher.LauncherSprite(name='__launcher__2',x=100, y=50, trigger_x=300, trigger_y=100))
    lb.addObject(Launcher.LauncherSprite(name='__launcher__3',x=300, y=250, trigger_x=50, trigger_y=300))
    #lb.addObject(Enemy.EnemySprite(x=160,y=300,width=15,height=15))
    lb.addObject(Friend.FriendSprite(x=50,y=160,width=50,height=50))
    lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=50,y=80,width=50,height=50))
    lb.addObject(Enemy.EnemySprite(x=300,y=100,width=50,height=50))
    lb.addObject(Star.StarSprite(x=100,y=100,width=20,height=20))
    #lb.addObject(Wizard.WizardSprite(x=300,y=50))
    lb.addObject(Wizard.WizardSprite(x=25,y=50))
    lb.render()
