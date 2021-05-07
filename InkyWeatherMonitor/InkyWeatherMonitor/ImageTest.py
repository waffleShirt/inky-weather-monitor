from inky import InkyWHAT, InkyMockWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

import os 

# Environment vars
from dotenv import load_dotenv
load_dotenv()
inkyEnv = os.environ.get('INKY_ENV')
updateInterval = 0 

inky_display = None 
if (inkyEnv == 'MOCK'):
	inky_display = InkyMockWHAT("black")
	updateInterval = 5
	inky_display.set_border(inky_display.RED)
elif (inkyEnv == 'REAL'):
	inky_display = InkyWHAT("black")
	updateInterval = 60
	inky_display.set_border(inky_display.BLACK)
else:
	print("You screwed up")

img = Image.new("P", (400, 300), 255)
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 36)


icon = Image.open("37-idx.png")
icon = icon.resize((100, 100), resample=Image.NONE)
pal_img = Image.new("P", (1, 1))
pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0))
icon = icon.convert("RGB").quantize(palette=pal_img)
img.paste(icon, (10,10))



#icon2 = Image.open("38-g3.png")
#icon2 = icon2.resize((100, 100), resample=Image.NONE)
#img.paste(icon2, (110,10))

## You can also just load the icons directly and convert them to greyscale, but they don't seem to end up looking as smooth as converting them in GIMP. I suspect this is because
## the image exported from GIMP has an explicit white background, whereas loading the PNG with transparency and converting doesn't work anywhere near as well. 
#icon3 = Image.open("41.png")
#icon3 = icon3.resize((100, 100), resample=Image.NONE)
#icon3 = icon3.convert("L")
#img.paste(icon3, (10,110))

#icon4 = Image.open("41-g.png")
#icon4 = icon4.resize((100, 100), resample=Image.NONE)
#img.paste(icon4, (110,110))

inky_display.set_image(img)
inky_display.show()

wait = input("Press enter to close") 

	

