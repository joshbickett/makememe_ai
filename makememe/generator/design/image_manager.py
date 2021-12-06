from PIL import Image, ImageDraw, ImageFont, ImageOps
from makememe.generator.design.font import font_path
from makememe.generator.prompts.helper import Helper


class Image_Manager:
  def __init__(self):
    print("Image manager create")
  
  @staticmethod
  def add_text(base, text, position, font_size, text_color, text_width_proportion=4, wrapped_width=None, rotate_degrees=None):

    if wrapped_width is not None: 
      text = Helper.wrap(text, wrapped_width)

    font = ImageFont.truetype(font_path, font_size)
    overlay_image =Image.new('L', (int(base.width/text_width_proportion), int(base.height/4)), 0)
    draw = ImageDraw.Draw(overlay_image)    
    draw.text((0, 0), text,  font=font, fill=255)

    if rotate_degrees is not None:
      overlay_image=overlay_image.rotate(rotate_degrees,  expand=1)

    color_value = (0,0,0)
    if text_color == "white": 
      color_value = (255,255,255)
    base.paste(ImageOps.colorize(overlay_image, (0,0,0), color_value), position, overlay_image)

    return base
