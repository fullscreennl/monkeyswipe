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
					<string>%(firstframe)s</string>
					<key>sheet_id</key>
					<integer>5</integer>
					<key>id</key>
					<integer>%(__objID__)s</integer>
					<key>name</key>
					<string>%(name)s</string>
					<key>classname</key>
					<string>%(classname)s</string>
                    <key>static</key>
                    <%(static)s/>
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

CONTACTS = """"""

class FriendSprite(PhysicsMixin.PhysicsMixin):
    
    def __init__(self,**kwargs):
        self.params = kwargs
        self.params['name'] = "Friend"
        self.process(kwargs)
        self.addDefault('classname','FriendSprite')
        #self.addDefault('firstframe','friend0001.png')
        try:
            self.params['classname']
            if self.params['classname'] == "AccelFriendSprite":
                self.params['firstframe'] = "accel_friend.png"
            else:
                raise "default"
        except:
            self.params['firstframe'] = "friend0001.png"
        self.params['__objID__'] = ID.next()
    
    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)
    
    
    
if __name__ == "__main__":
    print FriendSprite(x=160,y=10,width=100, height=100).render()[0]
    
