import config

config.EXPORT_PATH = "/Users/johantenbroeke/Sites/projects/fullscreen_3/xcodeprojects/oneonone/daily_leveldata/"
config.USE_BINARY_PLIST = 0

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
				    ("121", 16,60,"green_bg.png"),
				    ("122", 16,60,"blue_bg.png"),
				    ("123", 16,60,"grey_bg.png"),
				    ("124", 16,60,"yellow_bg.png"),
				    ("125", 16,60,"blue_bg.png"),
				    ("126", 16,60,"green_bg.png"),
				    ("131", 16,60,"grey_bg.png"),
				    ("132", 16,60,"blue_bg.png"),
				    ("138", 16,60,"green_bg.png"),
				    ("139", 16,60,"grey_bg.png"),
				    ("144", 16,60,"grey_bg.png"),
				    ("150", 16,60,"grey_bg.png"),
				    ("151", 16,60,"green_bg.png"),
				    ("155", 16,60,"yellow_bg.png"),
				    ("156", 16,60,"blue_bg.png"),
				    ("158", 16,60,"blue_bg.png"),
				    ("165", 16,60,"green_bg.png"),
				    ("166", 16,60,"green_bg.png"),
				    ("176", 16,60,"green_bg.png"),
				    ("177",16,160,"blue_bg.png"),
				    ("178",16,160,"grey_bg.png"),
				    ("179",16,160,"grey_bg.png"),
				    ("180",16,160,"grey_bg.png"),
				    ("189",16,160,"green_bg.png"),
				    ("The_Maze_You_Special",16,160,"green_bg.png"),
				    ("The_Pitcher",16,160,"green_bg.png"),
				    ("Smoke_Stack",16,160,"blue_bg.png"),
				    ("Nice_Moustache",16,160,"green_bg.png")
				    ]


for l in levels_to_render:
	module = __import__("daily_levels."+l[0],globals(), locals(), [l[0]], -1)
	level_name =  l[0]
	module.render(level_name,l[3])
