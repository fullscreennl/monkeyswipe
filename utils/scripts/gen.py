import Image
import ImageDraw
import ImageFont

for i in range(40):
	im = Image.open('background.png')
	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype("BudmoJiggler.TTF", 100)
	draw.text((10, 25), "level "+str(i+1), font=font)
	im.save("assets/background_"+str(i+1)+".png")

	#f = open('template.plist')
	#xml = f.read()
	#xml = xml.replace("<string>background_2.png</string>","<string>background_"+str(i+1)+".png</string>");
	#outfile = open("assets/level_"+str(i+1)+".plist",'w')
	#outfile.write(xml)
