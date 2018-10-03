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
					<string>spikey_buddy0001.png</string>
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
                <string>Enemy</string>
                <key>sprite2</key>
                <string>Spikey</string>
                <key>eventName</key>
                <string>onDestroy</string>
            </dict>
"""

class SpikeyBuddySprite(PhysicsMixin.PhysicsMixin):
    
    def __init__(self,**kwargs):
        self.params = kwargs
        self.params['name'] = "Spikey"
        self.process(kwargs)
        self.addDefault('classname','SpikeySprite')
        self.params['__objID__'] = ID.next()
    
    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)
    
    
    
if __name__ == "__main__":
    print SpikeyBuddySprite(x=160,y=10,width=100, height=100).render()[0]
    
