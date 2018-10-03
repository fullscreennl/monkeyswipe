import PhysicsMixin
import ID

BODIES = """
            <dict>
                <key>body</key>
                <dict>
                    <key>x</key>
                    <integer>%(x)s</integer>
                    <key>y</key>
                    <integer>%(y)s</integer>
                    <key>width</key>
                    <integer>50</integer>
                    <key>height</key>
                    <integer>30</integer>
                    <key>firstFrame</key>
                    <string>launcher_base.png</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>%(__objID__)s</integer>
                    <key>name</key>
                    <string>seat</string>
                    <key>static</key>
                    <true/>
                </dict>
                <key>shapes</key>
                <array>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>0</integer>
                        <key>width</key>
                        <integer>50</integer>
                        <key>height</key>
                        <integer>30</integer>
                        <key>type</key>
                        <string>rect</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>20</integer>
                        <key>restitution</key>
                        <real>0.2</real>
                    </dict>
                </array>
            </dict>

            <!-- this will be the piston -->
            <dict>
                <key>body</key>
                <dict>
                    <key>x</key>
                    <integer>%(x)s</integer>
                    <key>y</key>
                    <integer>%(piston_y)s</integer>
                    <key>width</key>
                    <integer>50</integer>
                    <key>height</key>
                    <integer>30</integer>
                    <key>firstFrame</key>
                    <string>launcher_piston.png</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>%(__objID2__)s</integer>
                    <key>name</key>
                    <string>%(name)s</string>
                    <key>static</key>
                    <false/>
                    <key>classname</key>
                    <string>LauncherSprite</string>
                </dict>
                <key>shapes</key>
                <array>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>0</integer>
                        <key>width</key>
                        <integer>50</integer>
                        <key>height</key>
                        <integer>30</integer>
                        <key>type</key>
                        <string>rect</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>20</integer>
                        <key>restitution</key>
                        <real>0.2</real>
                    </dict>
                </array>
            </dict>

            <!-- this will be the trigger -->
            <dict>
                <key>body</key>
                <dict>
                    <key>x</key>
                    <integer>%(trigger_x)s</integer>
                    <key>y</key>
                    <integer>%(trigger_y)s</integer>
                    <key>width</key>
                    <integer>15</integer>
                    <key>height</key>
                    <integer>15</integer>
                    <key>firstFrame</key>
                    <string>trigger.png</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>%(__objID3__)s</integer>
                    <key>name</key>
                    <string>%(name)s_trigger</string>
                    <key>static</key>
                    <true/>
                </dict>
                <key>shapes</key>
                <array>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>0</integer>
                        <key>width</key>
                        <integer>15</integer>
                        <key>height</key>
                        <integer>15</integer>
                        <key>type</key>
                        <string>circ</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>20</integer>
                        <key>restitution</key>
                        <real>0.2</real>
                    </dict>
                </array>
            </dict>
"""

JOINTS = """
           <dict>
                <key>type</key>
                <string>prismatic</string>
                <key>body1</key>
                <string>%(name)s</string>
                <key>motorSpeed</key>
                <real>10.0</real>
                <key>maxMotorTorque</key>
                <real>1000.0</real>
                <key>enableMotor</key>
                <false/>
                <key>lowerTranslation</key>
                <real>0</real>
                <key>upperTranslation</key>
                <real>30</real>
                <key>xdir</key>
                <real>0.0</real>
                <key>ydir</key>
                <real>1.0</real>
                <key>enableLimit</key>
                <true/>
            </dict>
"""

CONTACTS = """
            <dict>
                <key>sprite1</key>
                <string>Hero</string>
                <key>sprite2</key>
                <string>%(name)s_trigger</string>
                <key>eventName</key>
                <string>%(name)s</string>
            </dict>
"""

class LauncherSprite:

    def __init__(self,**kwargs):
        
        self.params = kwargs
        
        try:
            self.params['power'] = kwargs['power']
            self.params['name'] = kwargs['name'] + kwargs['power']
        except:
            self.params['power'] = '#1000'
            self.params['name'] = kwargs['name'] + '#1000'
            
        
        kwargs['piston_y'] = int(kwargs['y']) + 30 
        self.params['__objID__'] = ID.next()
        self.params['__objID2__'] = ID.next()
        self.params['__objID3__'] = ID.next()

    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)

if __name__ == "__main__":
    #print LauncherSprite(name='launcher_1',x=160,y=50,trigger_x=400, trigger_y=100,power="_hard").render()[2]
    #print LauncherSprite(name='launcher_1',x=160,y=50,trigger_x=400, trigger_y=100,power="_soft").render()[2]
    print LauncherSprite(name='launcher_1',x=160,y=50,trigger_x=400, trigger_y=100,power="_500").render()[0]
    #print LauncherSprite(name='launcher_1',x=160,y=50,trigger_x=400, trigger_y=100).render()[2]
