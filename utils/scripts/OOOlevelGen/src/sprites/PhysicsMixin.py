import sys
sys.path.append("..")

class PhysicsMixin:
    
    def addDefault(self,key,defaultValue):
        try:
            self.params[key]
        except:
            self.params[key] = defaultValue

    def process(self,args):

        try:
            self.params['r'] =  args['restitution']
        except:
            self.params['r'] = 0.2

        try: 
            self.params['f'] =  args['friction']
        except:
            self.params['f'] = 0.5

        try:
            self.params['d'] =  args['density']
        except:
            self.params['d'] = 20
            
        try:
            self.params['static'] =  args['static']
        except:
            self.params['static'] = 'false'
            
    def setName(self,name):
        self.name = name
        self.params['name'] = name
        return self
