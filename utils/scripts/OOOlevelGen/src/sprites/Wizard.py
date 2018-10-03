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
                    <integer>135</integer>
                    <key>firstFrame</key>
                    <string>wizard.png</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>%(__objID__)s</integer>
                    <key>name</key>
                    <string>%(name)s</string>
                    <key>static</key>
                    <false/>
                    <key>classname</key>
                    <string>%(classname)s</string>
                </dict>
                <key>shapes</key>
                <array>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>-43</integer>
                        <key>width</key>
                        <integer>50</integer>
                        <key>height</key>
                        <integer>50</integer>
                        <key>type</key>
                        <string>rect</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>20</integer>
                        <key>restitution</key>
                        <real>0.2</real>
                    </dict>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>200</integer>
                        <key>width</key>
                        <integer>12</integer>
                        <key>height</key>
                        <integer>100</integer>
                        <key>type</key>
                        <string>poly</string>
                        <key>points_CCW</key>
                        <string>25|-18#0|57#-25|-18</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>1</integer>
                        <key>restitution</key>
                        <real>0.5</real>
                    </dict>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>57</integer>
                        <key>width</key>
                        <integer>20</integer>
                        <key>height</key>
                        <integer>20</integer>
                        <key>type</key>
                        <string>circ</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>1</integer>
                        <key>restitution</key>
                        <real>0.5</real>
                        <key>userData</key>
                        <string>hat_top</string>
                    </dict>
                </array>
            </dict>
"""

JOINTS = """"""

CONTACTS = """"""

class WizardSprite(PhysicsMixin.PhysicsMixin):
    
    def __init__(self,**kwargs):
        self.params = kwargs
        self.params['name'] = "Wizard"
        self.params['__objID__'] = ID.next()
        self.addDefault('classname','')
    
    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)
    
    
    
if __name__ == "__main__":
    WizardSprite(x=160,y=10).render()
    
