from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Pompous(Prompt):
    name = "Pompous"
    description = "pompous"

    def __init__(self):
        self.instruction = '''
###
Message: People who run marathon think they are superior. Maybe that's the case
{"action":"Running marathon"}
###
Message: People who play chess seem to think they are better than people who play checkers
{"action":"People who play chess"}
###
Message: Coding gives people a feeling of being great
{"action":"Coding"}
###
Message: Shareholders that don't have to report to any managers and make money think it is great.
{"action":"Not reporting to any managers"}
###
Message: Being able to do a front flip makes people pompus
{"action":"Being able to do a front flip"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['action'], 10)

            d.text((30, 900),wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((30, 1125), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

