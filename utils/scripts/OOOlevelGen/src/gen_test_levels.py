import LevelBuilder
import config
import Image, ImageDraw, ImageFont

#this is to test the integration of new Levelpacks

from sprites import *

config.EXPORT_PATH = "/Users/johantenbroeke/Sites/projects/fullscreen_3/xcodeprojects/oneonone/Resources/leveldata_2/"

level_template = """
		<dict>
			<key>id</key>
			<string>%(name)s</string>
			<key>score</key>
			<integer>0</integer>
			<key>pic</key>
			<string>%(name)s.png</string>
			<key>levelTitle</key>
			<string>%(title)s</string>
			<key>par</key>
			<integer>%(par)s</integer>
			<key>tbl</key>
			<integer>%(tbl)s</integer>
		</dict>
"""

generated_levels = ""

def generatePreviewImage(name):
	im = Image.new('RGB',(240,160),(0,0,0))
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("fonts/BudmoJiggler.TTF", 10)
	draw.text((10, 25), name, font=font)
	im.save(config.EXPORT_PATH+name+".png")


for l in range(40):
    lb = LevelBuilder.LevelBuilder("level_"+str(l)+".plist", background="blue_bg.png")
    lb.addObject(Hero.HeroSprite(x=20,y=10))
    lb.addObject(Enemy.EnemySprite(x=160,y=25,width=50,height=50))
    lb.addObject(Star.StarSprite(x=400,y=100,width=20,height=20))
    lb.render()
    generated_levels += level_template%{'name':"leveldata_2/level_"+str(l+1), 'title':"level_"+str(l+1), 'par':60, 'tbl':60}
    generatePreviewImage("level_"+str(l+1))

level_data = open("gameprogress_template.plist").read()

level_data =  level_data%{'levels':generated_levels}


game_progress_output = open(config.GAMEPROGRESS_PATH+"gameprogress_2.plist",'w')
game_progress_output.write(level_data)
game_progress_output.close()
