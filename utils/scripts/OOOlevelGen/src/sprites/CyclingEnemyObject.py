import PhysicsMixin
import ID
import Enemy
import Friend
import Joints
import Contacts

class CyclingEnemyObjectSprite:

    def __init__(self,**kwargs):
        self.params = kwargs
        self.params['__objID__'] = ID.next()
        self.bodies = ""
        self.joints = ""
        self.contacts = ""
        self.buildBodies()
        self.buildJoints()
        self.buildContacts()

    def buildJoints(self):
        self.joints += Joints.RevoluteJoint(body1='inner_circ'+self.params['name'],
                                            body2='axel'+self.params['name'],
                                            motor_speed='1.0',
                                            torque='100000.0',
                                            enable_motor='false',
                                            lower_angle='12',
                                            upper_angle='45',
                                            enable_limit='false',
                                            collide_connected='false').render()[1]

        self.joints += Joints.RevoluteJoint(body1='rotor_enemy'+self.params['name'],
                                            body2='axel'+self.params['name'],
                                            motor_speed='5.0',
                                            torque='1000000.0',
                                            enable_motor='true',
                                            lower_angle='12',
                                            upper_angle='45',
                                            enable_limit='false',
                                            collide_connected='false').render()[1]
                                        
 
    def buildContacts(self):
        self.contacts = Contacts.Contact(body1='Hero',body2='rotor_enemy'+self.params['name'],event_name='onLose').render()[2]

    def buildBodies(self):
        self.center = Friend.FriendSprite(width=self.params['width'],
                                    height=self.params['height'],
                                    x= self.params['x'],
                                    y= self.params['y'],
                                    static="true",friction=20).setName('inner_circ'+self.params['name'])
        self.bodies += self.center.render()[0]
        self.joints += self.center.render()[1]
        self.contacts += self.center.render()[2]
     
        self.hub = Friend.FriendSprite(width=self.params['enemy_size']-3,
                                    height=self.params['enemy_size']-3,
                                    y= self.params['y'] + self.params['height']/2 + self.params['enemy_size']/2,
                                    x= self.params['x'],
                                    static="false",density=100).setName('axel'+self.params['name'])
        self.bodies += self.hub.render()[0]
        self.joints += self.hub.render()[1]
        self.contacts += self.hub.render()[2]
 
        self.outer = Enemy.EnemySprite(width=self.params['enemy_size'],
                                    height=self.params['enemy_size'],
                                    x= self.params['x'],
                                    y= self.params['y'] + self.params['height']/2 + self.params['enemy_size']/2 -2,
                                    static="false",density=100,friction=20).setName("rotor_enemy"+self.params['name'])
        self.bodies += self.outer.render()[0]
        self.joints += self.outer.render()[1]
        self.contacts += self.outer.render()[2]



    def render(self):
        return( self.bodies, self.joints, self.contacts)



if __name__ == "__main__":
    print CyclingEnemyObjectSprite(x=100,y=100,width=200, height=200,enemy_size=20).render()[0]
