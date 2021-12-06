from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Ineffective_Solution(Prompt):
    name = "Ineffective_Solution"
    description = "ineffective solution"

    def __init__(self):
        self.instruction = '''
###
Message: There is a bunch of traffic in town. The government decided to make the roads wider, but that's not the problem
{"attempted_solution":"more roads", "failure":"traffic"}
###
Message: Some people who brush their hair still get messy hair.
{"attempted_solution":"brush", "failure":"messy hair"}
###
Message: I go for a walk daily, but then I end up eating a donut. Pretty ineffective
{"attempted_solution":"walk daily", "failure":"eating a donut"}
###
Message: I drink coffee to be more awake, but then I can't sleep and I am tired the next day
{"attempted_solution":"drink coffee", "failure":"can't sleep and I am tired the next day"}
###
Message: I try to read a book to spend less time on my phone, but I end up googling concepts on my phone
{"attempted_solution":"read a book to spend less time on my phone", "failure":"end up googling concepts on my phone"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 50)
            watermark_font = ImageFont.truetype(font_path, 25)
            d = ImageDraw.Draw(txt)

            meme_text_one = Helper.wrap(meme_text['attempted_solution'], 15)
            meme_text_two = Helper.wrap(meme_text['failure'], 15)

            d.text((100, 100), meme_text_one, font=font, fill=(255, 255, 255, 255))
            d.text((100, 700), meme_text_two, font=font, fill=(255, 255, 255, 255))
            d.text((20, 1150), "makememe.ai", font=watermark_font, fill=(255, 255, 255, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

