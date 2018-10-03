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
                    <integer>%(width)s</integer>
                    <key>height</key>
                    <integer>%(height)s</integer>
                    <key>firstFrame</key>
                    <string>hero.png</string>
                    <key>sheet_id</key>
                    <integer>5</integer>
                    <key>id</key>
                    <integer>20</integer>
                    <key>name</key>
                    <string>%(name)s</string>
                    <key>classname</key>
                    <string>%(classname)s</string>
                </dict>
                <key>shapes</key>
                <array>
                    <dict>
                        <key>x</key>
                        <integer>0</integer>
                        <key>y</key>
                        <integer>0</integer>
                        <key>width</key>
                        <integer>%(width)s</integer>
                        <key>height</key>
                        <integer>%(height)s</integer>
                        <key>type</key>
                        <string>circ</string>
                        <key>friction</key>
						<real>%(f)s</real>
						<key>density</key>
						<integer>%(d)s</integer>
						<key>restitution</key>
						<real>%(r)s</real>
                    </dict>
                </array>
            </dict>
"""

JOINTS = """"""
CONTACTS = """
            <dict>
                <key>sprite1</key>
                <string>HeroSprite</string>
                <key>sprite2</key>
                <string></string>
                <key>eventName</key>
                <string>onHeroHit</string>
            </dict>
"""

class HeroSprite(PhysicsMixin.PhysicsMixin):
    
    def __init__(self,**kwargs):
        

        self.params = kwargs
        try:
            self.params['width'] = kwargs['width']
            self.params['height'] = kwargs['height']
        except:
            self.params['width'] = '30'
            self.params['height'] = '30'
            
        self.params['name'] = "Hero"
        self.process(kwargs)
        self.addDefault('classname','HeroSprite')
        self.params['__objID__'] = ID.next()
    
    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)
    
    
    
if __name__ == "__main__":
    print HeroSprite(x=160,y=10).render()[0]
    
