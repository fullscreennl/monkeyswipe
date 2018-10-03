import config
import Image
import ImageDraw
import ImageFont

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

				    ("Play_A_Lop", 4,60,"yellow_bg.png"),
				    ("Empty_The_Bucket", 20,60,"red_bg.png"),
				    ("Heavy_Friend", 12, 60,"blue_bg.png"), 
				    ("Bash_The_Beam", 8, 60,"red_bg.png"),
				    ("Crowd_Surfing",10, 60, "grey_bg.png"),
				    ("Just_Push",36, 100, "blue_bg.png"),
				    ("Heavy_Dudes", 18,60,"grey_bg.png"),
				    ("Tower_Of_Power", 8,60,"green_bg.png"),
				    ("Off_The_Wall",10, 60, "blue_bg.png"),
				    # PREMIUM #
					("Balance_Boy",12, 60, "grey_bg.png"),
					("All_Nuts_And_Beams",15,60,"yellow_bg.png"),
					("One_Wiggle",4, 60, "grey_bg.png"),
					("Great_Unleash",24,28,"yellow_bg.png"),
					("Cableway",30, 60, "blue_bg.png"),
					("Enemy_Dispenser",10,60,"grey_bg.png"),
                    ("Chain_Of_Evil", 12,20,"purple_bg.png"),
					("Enemies_in_Orbit",10, 60, "blue_bg.png"),
                    ("Temple_Of_Boom", 10,60,"grey_bg.png"),
                    ("Rotational_Problems", 15,60,"green_bg.png"),
                    ("Swing_Spikey", 10,60,"yellow_bg.png"),
                    ("Swing_when_you_Win",60,43,"red_bg.png"),
				    ("Logicz", 200,243,"grey_bg.png"),
				    ("Launch_Base", 60,120,"grey_bg.png"),
				    ("Meet_The_Wizard", 10,60,"green_bg.png"),
				    ("Chain_Surfing", 16,60,"grey_bg.png"),
                    ("Pinball_Machine",60,60,"green_bg.png"),
                    ("Launch_Your_Enemies", 8,28,"yellow_bg.png"),
					("Bombs_Ahead",10,60,"red_bg.png"),
					("Ball_Time",12,60,"red_bg.png"),
					("Stuff_of_Damocles",28,48,"green_bg.png"), 
					("Monkey_Swing", 32,44,"blue_bg.png"),
					("Systematic_Overload",48,64,"purple_bg.png"),
					("Dutch_Windmill", 10,60,"blue_bg.png"),
					("Atomic_Wax", 160,160,"yellow_bg.png"),
					("Its_All_Diagonals",56,68,"blue_bg.png"),
					("Destroying_the_Balance",140,107,"red_bg.png"),
				    ("Volleyball_Spikey", 24,80,"purple_bg.png"),
                    ("Piramid_Of_Egypt",32, 32, "green_bg.png"),
				    ("The_Grand_Final",400, 400, "blue_bg.png")
				    ]

level_data = open("gameprogress_template.plist").read()
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
	level_title = level_name.replace("_"," ")
	module.render(level_name,l[3])
	
	generated_levels += level_template%{'name':level_name, 'title':level_title, 'par':l[1], 'tbl':l[2]}

level_data =  level_data%{'levels':generated_levels}


game_progress_output = open(config.GAMEPROGRESS_PATH+"gameprogress.plist",'w')
game_progress_output.write(level_data)
game_progress_output.close()
