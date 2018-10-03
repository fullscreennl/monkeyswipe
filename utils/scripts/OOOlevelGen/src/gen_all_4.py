import config
import Image
import ImageDraw
import ImageFont
import shutil
import ms_score

config.EXPORT_PATH = "/Users/johantenbroeke/Sites/projects/fullscreen_3/xcodeprojects/oneonone/Resources/leveldata_4/"

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
("Dodge_It", 3,3,"red_bg.png"),
("Bump", 7,11,"purple_bg.png"),
("Little_Buddha", 5,1,"yellow_bg.png"),
("Hexagram", 25,5,"yellow_bg.png"),
("Part_Of_A_Chain", 6,10,"yellow_bg.png"),
("Our_House", 41,26,"green_bg.png"),
("One_Too_Many", 75,21,"yellow_bg.png"),
("Are_Those_pigs", 47,22,"blue_bg.png"),
("Its_A_Long_Way", 25,10,"green_bg.png"),
("Climb_Up", 2,19,"grey_bg.png"),
("The_Bridge_Too_Far", 2,1,"purple_bg.png"),
("Connected", 27,13,"purple_bg.png"),
("The_Carrier", 26,11,"red_bg.png"),
("Pinball_Madness", 32,16,"blue_bg.png"),
("Mission_Impossible", 11,6,"green_bg.png"),
("HimmelBau", 7,4,"grey_bg.png"),
("Crowded_House", 19,9,"yellow_bg.png"),
("Cant_Move", 1,80,"red_bg.png"),
("Stay_Mellow", 1,10,"grey_bg.png"),
("Multi_Ball", 24,6,"red_bg.png"),
("Another_Bombtrack", 66,26,"blue_bg.png"),
("Hole_In_The_Floor", 23,17,"blue_bg.png"),
("House_With_A_View", 100,37,"purple_bg.png"),
("World_Tower_Fund", 21,11,"yellow_bg.png"),
("It_Can_Be_Done", 80,50,"yellow_bg.png"),
("Monkey_in_Wonderland", 30,14,"red_bg.png"),
("Diabolic_Car", 20,22,"grey_bg.png"),
("Rise_Above", 2,72,"green_bg.png"),
("Keep_Em_Rolling", 35,34,"purple_bg.png"),
("No_Escape", 6,4,"blue_bg.png"),
("It_Dont_Mean_A_Thing", 24,18,"green_bg.png"),
("Surf_Safari", 9,5,"blue_bg.png"),
("I_Can_Feel_Tension", 18,8,"yellow_bg.png"),
("Coming_From_Above", 20,5,"red_bg.png"),
("Come_And_Get_It", 2,1,"grey_bg.png"),
("Strange_Rotors", 22,12,"purple_bg.png"),
("Anger_Management", 20,10,"yellow_bg.png"),
("Domino_D_Day", 70,50,"purple_bg.png"),
("Destroy_The_Dangler", 8,8,"red_bg.png"),
("Chop_Chop_Burito", 20,100,"red_bg.png")
				    ]

level_data = open("gameprogress_template_no_tut.plist").read()
generated_levels = ""

def generatePreviewImage(name):
	im = Image.new('RGB',(240,160),(0,0,0))
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("fonts/BudmoJiggler.TTF", 10)
	draw.text((10, 25), name, font=font)
	im.save(config.EXPORT_PATH+name+".png")


for l in levels_to_render:
	module = __import__("levels."+l[0],globals(), locals(), [l[0]], -1)
	#print module
	level_name =  l[0]
	#generatePreviewImage(level_name)
	shutil.copyfile("level_screen_shots/"+level_name+".png",config.EXPORT_PATH+level_name+".png")
	level_title = level_name.replace("_"," ")
	module.render(level_name,l[3])
	
	pars = ms_score.calc3StarScoreForSwipes(l[1],l[2])
	generated_levels += level_template%{'name':"leveldata_4/"+level_name, 'title':level_title, 'par':pars[0], 'tbl':pars[1]}

level_data =  level_data%{'levels':generated_levels}


game_progress_output = open(config.GAMEPROGRESS_PATH+"gameprogress_4.plist",'w')
game_progress_output.write(level_data)
game_progress_output.close()
