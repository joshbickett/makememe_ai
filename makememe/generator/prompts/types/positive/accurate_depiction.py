from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Accurate_Depiction(Prompt):
    name = "Accurate_Depiction"
    description = "accurate depiction"

    def __init__(self):
        self.instruction = '''
###
Message: They told me I am too interested in crypto currencies and they couldn't be more right
{"depiction":"You are too interested in crypto currencies"}
###
Message: I had a fortune cookie tell me I code too much and It is so correct.
{"depiction":"You code too much"}
###
Message: You want to hear an accurate depiction. I am not running enough.
{"depiction":"You are not running enough"}
###
Message: They don't go outside enough. They need to get some sunlight. It's the truth
{"depiction":"They need to go outside more"}
###
Message: Humans making memes ok, AI making memes awesome.
{"depiction":"You want AI making memes"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 30)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['depiction'], 15)

            d.text((400, 780),wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((10, 1150), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

