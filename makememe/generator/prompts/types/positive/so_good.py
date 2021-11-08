from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class So_Good(Prompt):
    name = "So_Good"
    description = "so good"

    def __init__(self):
        self.instruction = '''
###
Message: The new Tesla robot is so cool
{"message":"A new Telsa robot"}
###
Message: The SpaceX Starship may launch next month and I couldn't be more excited
{"message":"The SpaceX Starship may launch next month"}
###
Message: Brownies with milk are my favorite thing on the planet
{"message":"Eat some brownies with milk"}
###
Message: Playing music with a band makes me truely happy
{"message":"Go play music with a band"}
###
Message: The new Daft Punk album is so good
{"message":"A new Daft Punk"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 55)
            watermark_font = ImageFont.truetype(font_path, 25)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['message'], 15)

            d.text((200, 200),wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((10, 1100), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

