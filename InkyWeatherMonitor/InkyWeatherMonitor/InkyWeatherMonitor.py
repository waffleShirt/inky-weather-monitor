from inky import InkyMockWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

inky_display = InkyMockWHAT("red")
inky_display.set_border(inky_display.RED)

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype(FredokaOne, 36)

from PersonalData import PersonalData
from ForecastData import ForecastData

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
inky_display.set_image(img)
inky_display.show()

img = Image.open("testimg2.png")
inky_display.set_image(img)
inky_display.show()

wait = input("Press enter to close") 
