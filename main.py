from math import radians, cos, sin

from PIL import Image, ImageDraw

image = Image.new('RGBA', (960, 960), (255, 255, 255))

draw = ImageDraw.Draw(image)

angle = radians(10 * (5 + 1))


with open('DS5.txt') as file:
    for line in file:
        coordArray = list(map(int, line.split()))
        x = cos(angle) * (coordArray[1] - 480) - sin(angle) * (coordArray[00] - 480)
        y = sin(angle) * (coordArray[1] - 480) + cos(angle) * (coordArray[0] - 480)
        draw.line((x + 480, y + 480, x + 481, y + 481), fill=(15, 10, 222))

image.show()
image.save('DS5.png', "PNG")
