from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path

class Waiting(Prompt):
    name = "Waiting"
    description = "waiting"

    def __init__(self):
        self.instruction = '''
###
Message: I've been waiting for SpaceX to launch the starship for ever
{"waiting_on": "SpaceX Startship"}
###
Message: I can't wait for makememe.ai to launch, but it's taking a little while
{"waiting_on": "makememe.ai"}
###
Message: Drakes new album is going to be fire. Why do I have to wait
{"waiting_on": "Drakes new album"}
###
Message: I want to create an NFT, but opensea.com is taking a while to load
{"waiting_on": "opensea.com"}
###
'''
    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['waiting_on'], 20)

            d.text((800, 800), wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((10, 1000), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name
