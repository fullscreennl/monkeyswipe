import config
import Image
import ImageDraw
import ImageFont
import shutil
import ms_score

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

levels_to_render = [
("Timing_Is_Key", 1,1,"green_bg.png"),	
("Big_Fella", 3,9,"grey_bg.png"),
("Kick_Spikey", 2,3,"green_bg.png"),			    
("Its_Just_A_Bomb", 2,5,"red_bg.png"),
("A_Swinging_Star", 3,3,"grey_bg.png"),
("Eifel_Brought_Us_Tower", 3,2,"blue_bg.png"),
("He_Is_Swinging", 4,2,"blue_bg.png"),
("Easy_Peacy", 6,12,"red_bg.png"),
("Chevy_To_The_Levy", 11,13,"grey_bg.png"),
("It_Looks_Easy", 4,2, "yellow_bg.png"),
("Jos_Brink_Memorial_BBQ", 7,6,"green_bg.png"),
("It_A_jungle_In_Here", 19,8,"purple_bg.png"),
("Mind_The_Blades", 5,4,"green_bg.png"),
("Bouncy_Bouncy", 7,6,"yellow_bg.png"),
("Bound_Together", 1,1,"green_bg.png"),
("Watch_Out", 9,12,"green_bg.png"),
("Loads_Of_Enemies", 5,5,"green_bg.png"),
("The_Hitman", 4,4,"green_bg.png"),
("Easy_Does_It", 6,4,"yellow_bg.png"),
("Wired", 2,5,"purple_bg.png"),
("Release_The_Cheese", 7,8,"blue_bg.png"),
("Jump_Up_And_Get_Down", 3,3,"green_bg.png"),
("Escape_From_Alcatel", 10,12,"green_bg.png"),
("Clockwork_Monkey", 5,5,"grey_bg.png"),
("Blade_Walker", 3,6,"purple_bg.png"),
("Huh_What_Now", 12,9,"green_bg.png"),
("Swing_A_Beam", 10,7,"yellow_bg.png"),
("Captain_Caveman", 4,3,"grey_bg.png"),
("A_Mazing", 86,76,"blue_bg.png"),
("The_Maze_You_Special", 24,18,"red_bg.png"),
("The_M_Lost_His_Mind", 2,2,"yellow_bg.png"),
("Unfriendly_Family", 7,3,"grey_bg.png"),
("Dropping_Bars", 3,4,"purple_bg.png"),
("The_Swing", 7,14,"green_bg.png"),
("X_Games", 11,9,"grey_bg.png"),
("Kick_Out_The_Jams", 3,5,"red_bg.png"),
("Thunder_Struck", 1,2,"grey_bg.png"),
("Wabi_Sabi", 6,7,"blue_bg.png"),
("Free_Willy", 3,7,"yellow_bg.png")

			    ]

level_data = open("gameprogress_template_easy.plist").read()
generated_levels = ""

def generatePreviewImage(name):
	im = Image.new('RGB',(240,160),(0,0,0))
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("fonts/BudmoJiggler.TTF", 10)
	draw.text((10, 25), name, font=font)
	im.save(config.EXPORT_PATH+name+".png")

level_counter = 1
for l in levels_to_render:
	level_counter += 1
	module = __import__("levels."+l[0],globals(), locals(), [l[0]], -1)
	#print module
	level_name =  l[0]
	#generatePreviewImage(level_name)
	try:
		shutil.copyfile("level_screen_shots/"+level_name+".png",config.EXPORT_PATH+level_name+".png")
	except:
		print "no screenshot ! "+level_name +":"+str(level_counter)
	level_title = level_name.replace("_"," ")
	module.render(level_name,l[3])
	pars = ms_score.calc3StarScoreForSwipes(l[1],l[2])
	generated_levels += level_template%{'name':"leveldata_2/"+level_name, 'title':level_title, 'par':pars[0], 'tbl':pars[1]}

#print generated_levels
level_data =  level_data%{'levels':generated_levels}

shutil.copyfile("level_screen_shots/tutorial_1.plist",config.EXPORT_PATH+"tutorial_1.plist")
shutil.copyfile("level_screen_shots/tutorial_2.plist",config.EXPORT_PATH+"tutorial_2.plist")


game_progress_output = open(config.GAMEPROGRESS_PATH+"gameprogress_2.plist",'w')
game_progress_output.write(level_data)
game_progress_output.close()
