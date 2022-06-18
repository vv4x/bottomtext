#bottomtext3
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
from io import BytesIO

rawtext = input('what bottomtext: ')
path = 'kitty.png'

text = rawtext.upper()

textsize = 80

image = Image.open(path)
draw = ImageDraw.Draw(image)

with Image.open(path) as img:
    width, height = img.size

font = ImageFont.truetype('impact.ttf', size = textsize)

draw.text((width // 2, height / 35),text, font = font, fill = (0,0,0), align = 'center', anchor = 'mt', stroke_width = 5, stroke_fill = (255,255,255))
draw.text((width // 2, height - textsize ),'BOTTOM TEXT', font = font, fill = (0,0,0), align = 'center', anchor = 'mt', stroke_width = 5, stroke_fill = (255,255,255))

image.save('bottomtext1.png')


