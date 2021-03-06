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

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 36)

from PersonalData import PersonalData
from ForecastData import ForecastData

# Timer imports
import sched, time 
s = sched.scheduler(time.time, time.sleep)

def do_something(sc):
	print("Doing stuff")
	s.enter(updateInterval, 1, do_something, (sc,))

def UpdateDisplay(pd):
	pd.GetCurrentData() 
	currTemp = str(pd.currentData['observations'][0]['metric']['temp'])

	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	print("Update Display at: " + current_time + " - Temp: " + currTemp)
	
	# Clear the image buffer
	img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	draw = ImageDraw.Draw(img)

	#currTemp = str(pd.currentData['observations'][0]['metric']['temp'])
	currTempString = "Temp: " + currTemp + "C"
	x = 50
	y = 50
	draw.text((x, y), currTempString, inky_display.BLACK, font)
	inky_display.set_image(img)
	inky_display.show()

	#pd.currentData['observations'][0]['metric']['temp'] -= 0.1

	# Setup the function to run again
	s.enter(updateInterval, 1, UpdateDisplay, (pd,))

PD = PersonalData() 
PD.LoadAPIKey()
PD.GetCurrentData() 

FD = ForecastData()
FD.LoadAPIKey()
FD.LoadGeoCode()
FD.GetForecastData()

message = "Hello, World!"
w, h = font.getsize(message)
x = (inky_display.WIDTH / 2) - (w / 2)
y = (inky_display.HEIGHT / 2) - (h / 2)

draw.text((x, y), message, inky_display.RED, font)

message2 = "Poop"
w, h = font.getsize(message2)
x = 200
y = 200
draw.text((x,y), message2, inky_display.RED, font)

#inky_display.set_image(img)
#inky_display.show()

# So far this is the best looking setup for icons. Open the original icon in GIMP and set it to indexed using the Inky palette.
# Export image as PNG with background colour saved (as white?). The image will show as all white in the windows image viewer, but when it loads
# on the Inky screen the actual icon will be a solid black, and the background will be white. Converting the image to RGBA and using the image itself
# as the mask is why this works. All white pixels are copied into the new image, any black pixels if they existed would preserve the orignal pixel in
# the image being copied to. Anything else in between would create trnasparency effects. See the Paste An Image section on this page: http://docs.pimoroni.com/inkyphat/
# This won't work for coloured images, as the non white/black pixels will create a transparency effect. For now it works, but should be considered pretty hacky. 

# Ok, everything I said above is a total lie. The icons look signficantly better in greyscale. Open icons in GIMP. Image->Mode->Greyscale. Layer->Transparency->Remove alpha channel
# Load image and resize as required, then past into image buffer. Simple, that didn't need to take all evening to decide on, did it?
icon = Image.open("38c.png")
icon = icon.resize((100, 100), resample=Image.NONE)
pal_img = Image.new("PA", (1, 1))
#pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)
icon = icon.convert("RGBA")#.quantize(palette=pal_img)
img.paste(icon, (10,10), icon)

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

#UpdateDisplay(PD) 

#s.enter(5, 1, UpdateDisplay, (PD,))
#s.run()

wait = input("Press enter to close") 

	
