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
					<string>%(texture)s</string>
					<key>sheet_id</key>
					<integer>5</integer>
					<key>id</key>
					<integer>%(__objID__)s</integer>
					<key>name</key>
					<string>%(name)s</string>
                    <key>angle</key>
                    <integer>%(angle)s</integer>
                    <key>static</key>
                    <%(static)s/>
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
						<string>rect</string>
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

class BeamSprite(PhysicsMixin.PhysicsMixin):
    
    def __init__(self,**kwargs):
        self.params = kwargs
        self.asp = kwargs['width'] / float(kwargs['height'])
        if self.asp > 6:
            self.params['texture'] = "bar_long.png"
        elif self.asp <= 1:
            self.params['texture'] = "cube.png"
        else:
            self.params['texture'] = "bar.png"
        self.params['name'] = "Beam"
        self.process(kwargs)
        self.addDefault('classname','')
        self.params['__objID__'] = ID.next()
    
    def render(self):
        return( BODIES%self.params, JOINTS%self.params,CONTACTS%self.params)
    
    
    
if __name__ == "__main__":
    print BeamSprite(x=160,y=10,width=100, height=100, static='true',classname='UltraBeam',angle=45).render()[0]
    print BeamSprite(x=160,y=10,width=100, height=4, static='true',classname='UltraBeam',angle=45).render()[0]
    print BeamSprite(x=160,y=10,width=100, height=30, static='true',classname='UltraBeam',angle=45).render()[0]
    
