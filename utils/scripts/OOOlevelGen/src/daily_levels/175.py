import LevelBuilderfrom sprites import *def render(name,bg):	lb = LevelBuilder.LevelBuilder(name+".plist",background=bg)	lb.addObject(Hero.HeroSprite(x=240, y=80,width=32,height=32))	lb.addObject(Friend.FriendSprite(x=240, y=0,width=102,height=102,density=100,angle='0'))	lb.addObject(Joints.DistanceJoint(body1='Hero',body2='Friend',damping='0.2',freq='.6'))	lb.addObject(Beam.BeamSprite(x=416, y=208,width=127,height=14,static='true',angle='0'))	lb.addObject(Bomb.BombSprite(x=464, y=17,width=32,height=32))	lb.addObject(Beam.BeamSprite(x=64, y=208,width=127,height=14,static='true',angle='0'))	lb.addObject(SpikeyBuddy.SpikeyBuddySprite(x=451, y=237,width=40,height=40))	lb.render()