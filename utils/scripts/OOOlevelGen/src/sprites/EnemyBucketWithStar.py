import PhysicsMixin
import ID
import Beam
import Nut
import Enemy
import Star

class EnemyBucketWithStarSprite:
    
    def __init__(self,**kwargs):
        self.params = kwargs
        self.params['__objID__'] = ID.next()
        self.bodies = ""
        self.joints = ""
        self.contacts = ""
        self.buildWalls()
        self.buildNuts()
        self.fillWithEnemiesAndStar()
        
    def buildWalls(self):
        self.beam_left = Beam.BeamSprite(width=self.params['height'],
                                    height=15,
                                    x= self.params['x'] -self.params['width']/2,
                                    y= self.params['y'],
                                    angle = 100,
                                    static="true");
        self.bodies += self.beam_left.render()[0]
        self.joints += self.beam_left.render()[1]
        self.contacts += self.beam_left.render()[2]
        
        self.beam_right = Beam.BeamSprite(width=self.params['height'],
                                    height=14,
                                    x= self.params['x'] + self.params['width']/2,
                                    y= self.params['y'],
                                    angle = 80,
                                    static="true");
        self.bodies += self.beam_right.render()[0]
        self.joints += self.beam_right.render()[1]
        self.contacts += self.beam_right.render()[2]
        
        self.beam_bottom = Beam.BeamSprite(width= self.params['width'],
                                    height = 15,
                                    x= self.params['x'],
                                    y= self.params['y'] - self.params['height']/2 -10,
                                    angle=0,
                                    static="false",density=30);
        self.bodies += self.beam_bottom.render()[0]
        self.joints += self.beam_bottom.render()[1]
        self.contacts += self.beam_bottom.render()[2]
        
    def buildNuts(self):
        nut = Nut.NutSprite(x=self.params['x'] -self.params['width']/2 + 15,
                            y=self.params['y'] - self.params['height']/2 -20, density=30)
        self.bodies += nut.render()[0]
        self.joints += nut.render()[1]
        #self.contacts += nut.render()[2]
        
        nut = Nut.NutSprite(x=self.params['x'] + self.params['width']/2 -15,
                            y=self.params['y'] - self.params['height']/2 -20, density=30)
        self.bodies += nut.render()[0]
        self.joints += nut.render()[1]
        self.contacts += nut.render()[2]
        
    def fillWithEnemiesAndStar(self):
        for c in range(self.params['num_enemies']):
            enemy = Enemy.EnemySprite(width=self.params['enemy_size'], 
                                      height=self.params['enemy_size'], 
                                      x = self.params['x'] , 
                                      y=self.params['y']+ 30, 
                                      density=1 )
            self.bodies += enemy.render()[0]
            self.joints += enemy.render()[1]
        self.contacts += enemy.render()[2]
            
        star = Star.StarSprite(x = self.params['x'],
                               y=self.params['y'],
                               width=self.params['enemy_size'], 
                               height=self.params['enemy_size'])
        self.bodies += star.render()[0]
        self.joints += star.render()[1]
        self.contacts += star.render()[2]
    
    
    def render(self):
        return( self.bodies, self.joints, self.contacts)
    
    
    
if __name__ == "__main__":
    print EnemyBucketWithStarSprite(x=100,y=100,width=100, height=100,num_enemies=25,enemy_size=20).render()[0]
