import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageChops
from makememe.generator.design.font import font_path
from makememe.generator.prompts.helper import Helper


class Image_Manager:
  def __init__(self):
    print("Image manager create")
  
  @staticmethod
  def add_text(base, text, position, font_size, text_color="black", text_width_proportion=4, wrapped_width=None, rotate_degrees=None):
  
    try: 
      overlay_image = Image.new("RGBA", base.size, (0, 0, 0, 0))
      if wrapped_width is not None: 
        text = Helper.wrap(text, wrapped_width)

      font = ImageFont.truetype(font_path,font_size)
      draw = ImageDraw.Draw(overlay_image)
      draw.text(position, text, font=font, fill=(0, 0, 0, 255))
      if rotate_degrees is not None: 
        overlay_image = overlay_image.rotate(rotate_degrees)

      return overlay_image
    except Exception as e:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print(f'error: {e}')
      print(f'line: {exc_tb.tb_lineno}')
      print(f'file: {fname}')
      return "error"
    
