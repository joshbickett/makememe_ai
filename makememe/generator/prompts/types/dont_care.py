from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Dont_Care(Prompt):
    name = "Dont_Care"
    description = "don't care"

    def __init__(self):
        self.instruction = '''
###
Message: Doesn't matter to me that facebook is buying oculus
{"action":"Facebook buying oculus"}
###
Message: I dislike going running, it is so much work.
{"action":"Going running"}
###
Message: Doing laundry is the worst, I really don't care for it
{"action":"Doing laundry"}
###
Message: Some people cut in line and don't care about others
{"action":""Cutting in line"}
###
Message: We should all wear sunscreen, but some people don't seem to care
{"action":"wearing sunscreen"}
###
Message: Getting patents is sometimes important, but sometimes it is not at all
{"action":"getting patents"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['action'], 10)

            d.text((100, 175),wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((800, 1000), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

