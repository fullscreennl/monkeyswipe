import PhysicsMixin
import ID
from sprites.Beam import CONTACTS

BODIES = """
            <dict>
                <key>body</key>
                <dict>
                    <key>x</key>
                    <integer>%(x)s</integer>
                    <key>y</key>
                    <integer>%(y)s</integer>
                    <key>width</key>
                    <integer>100</integer>
                    <key>height</key>
                    <integer>100</integer>
                    <key>firstFrame</key>
                    <string>%(texture)s</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>%(__objID__)s</integer>
                    <key>name</key>
                    <string>%(__objID__)s_rotor</string>
                    <key>classname</key>
                    <string>RotorSprite</string>
                </dict>
                <key>shapes</key>
                <array>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>0</integer>
                        <key>width</key>
                        <integer>100</integer>
                        <key>height</key>
                        <integer>12</integer>
                        <key>type</key>
                        <string>rect</string>
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
                        <integer>0</integer>
                        <key>width</key>
                        <integer>12</integer>
                        <key>height</key>
                        <integer>100</integer>
                        <key>type</key>
                        <string>rect</string>
                        <key>friction</key>
                        <real>0.5</real>
                        <key>density</key>
                        <integer>1</integer>
                        <key>restitution</key>
                        <real>0.5</real>
                    </dict>
                </array>
            </dict>
            
            <!-- hinge of rotor-->
            
            <dict>
                <key>body</key>
                <dict>
                    <key>x</key>
                    <integer>%(x)s</integer>
                    <key>y</key>
                    <integer>%(y)s</integer>
                    <key>width</key>
                    <integer>10</integer>
                    <key>height</key>
                    <integer>10</integer>
                    <key>firstFrame</key>
                    <string>nut.png</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>%(__objID2__)s</integer>
                    <key>name</key>
                    <string>%(__objID2__)s_hinge</string>
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
                        <integer>10</integer>
                        <key>height</key>
                        <integer>10</integer>
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
                <string>revolute</string>
                <key>body1</key>
                <string>%(__objID2__)s_hinge</string>
                <key>body2</key>
                <string>%(__objID__)s_rotor</string>
                <key>motorSpeed</key>
                <real>%(speed)s</real>
                <key>maxMotorTorque</key>
                <real>%(torque)s</real>
                <key>enableMotor</key>
                <true/>
                <key>lowerAngle</key>
                <real>5</real>
                <key>upperAngle</key>
                <real>2</real>
                <key>enableLimit</key>
                <false/>
                <key>collideConnected</key>
                <false/>
                <key>userData</key>
                <string>rotor_joint</string>
            </dict>

"""
CONTACTS = """"""

class RotorSprite:
    
    def __init__(self, **kwargs):
        self.params = kwargs
        if kwargs['speed'] > 5:
            self.params['texture'] = "rotor2.png"
        else:
            self.params['texture'] = "rotor.png"
        self.params['__objID__'] = ID.next()
        self.params['__objID2__'] = ID.next()
    
    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)
    
    
    
    
    
if __name__ == "__main__":
    xml = RotorSprite(x=160, y=10, speed=200, torque=10000).render()
    print xml[0]
    print xml[1]
    
    
