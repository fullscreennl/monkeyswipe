import config
import Image
import ImageDraw
import ImageFont
import shutil
import ms_score

config.EXPORT_PATH = "/Users/johantenbroeke/Sites/projects/fullscreen_3/xcodeprojects/oneonone/Resources/leveldata_3/"

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
("Accelerate_Now", 4,12,"red_bg.png"),
("Nice_Moustache", 8,7,"yellow_bg.png"),
("Beat_The_Bugger", 9,8,"green_bg.png"),
("Up_The_Shaft", 6,4,"yellow_bg.png"),
("Wired_Again", 8,7,"red_bg.png"),
("AI_Enemy", 12,7,"purple_bg.png"),
("The_Follower", 24,5,"red_bg.png"),
("Bombs_Ahead", 15,11,"purple_bg.png"),
("They_Will_Get_You", 9,3,"grey_bg.png"),
("Will_It_Blend", 4,3,"yellow_bg.png"),
("Jump_Ramp", 14,17,"grey_bg.png"),
("Tumbling_Down", 10,10,"blue_bg.png"),
("Chained_Reaction", 14,4,"blue_bg.png"),
("Fly_Flies", 12,4,"green_bg.png"),
("Bouncer", 3,2,"red_bg.png"),
("Friendly_Push", 13,22,"blue_bg.png"),
("Triple_Touch", 15,7,"blue_bg.png"),
("Get_In_The_Car", 10,3,"blue_bg.png"),
("I_Can_See_Spikey", 36,21,"grey_bg.png"),
("Dazzling_With_BS", 6,5,"yellow_bg.png"),
("Daily_Mahal", 29,21,"green_bg.png"),
("Bump_The_Chump", 16,8,"yellow_bg.png"),
("Fast_Eddy", 4,2,"red_bg.png"),
("What_The_Bomb", 1,6,"green_bg.png"),
("Twelve_Monkies", 41,11,"green_bg.png"),
("Muchos_Nachos", 60,46,"purple_bg.png"),
("Tumble_Drop", 9,4,"purple_bg.png"),
("Connected_To_Spikey", 28,11,"blue_bg.png"),
("Chain_Reaction", 18,6,"green_bg.png"),
("Just_Swing", 24,14,"yellow_bg.png"),
("Surfs_Up", 17,7,"red_bg.png"),
("The_Hardest_Button", 13,7,"purple_bg.png"),
("Keep_Em_Save", 18,13,"grey_bg.png"),
("Seen_Before", 4,2,"purple_bg.png"),
("Were_Are_The_Boids", 10,7,"blue_bg.png"),
("Robocod", 23,9,"grey_bg.png"),
("Rag_Doll", 9,14,"red_bg.png"),
("What_The_Font", 15,21,"yellow_bg.png"),
("Total_Workout", 11,20,"purple_bg.png"),
("Wip_Wap", 1,100,"blue_bg.png")
				    ]

level_data = open("gameprogress_template_no_tut.plist").read()
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
	try:
		shutil.copyfile("level_screen_shots/"+level_name+".png",config.EXPORT_PATH+level_name+".png")
	except:
		print "no screenshot ! "+level_name +":"+str(level_counter)
	#generatePreviewImage(level_name)
	level_title = level_name.replace("_"," ")
	module.render(level_name,l[3])
	
	pars = ms_score.calc3StarScoreForSwipes(l[1],l[2])
	generated_levels += level_template%{'name':"leveldata_3/"+level_name, 'title':level_title, 'par':pars[0], 'tbl':pars[1]}

level_data =  level_data%{'levels':generated_levels}


game_progress_output = open(config.GAMEPROGRESS_PATH+"gameprogress_3.plist",'w')
game_progress_output.write(level_data)
game_progress_output.close()
