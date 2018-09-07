from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
xcoordinates = range(100, 600, 10)

myredcircle = CircleAsset(5, thinline, red)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x, x*-0.7 + 454)) for x in xcoordinates]
redsprites = [Sprite(myredcircle, (x, x*1.1 - 50)) for x in xcoordinates]

myapp = App()
myapp.run()
