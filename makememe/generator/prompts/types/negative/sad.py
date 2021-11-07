from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path

class Sad(Prompt):
    name = "Sad"
    description = "sad"

    def __init__(self):
        self.instruction = '''
###
Message: We still haven't been to Mars and it makes me cry
{"sad_part": "We still haven't been to Mars"}
###
Message: My college degree didn't get me a job and now I am in debt
{"sad_part": "Your college degree didn't get you a job and now you're in debt"}
###
Message: I have to actually read to learn something
{"sad_part": "You have to actually read to learn something"}
###
Message: I will never be famous and it's tragic
{"sad_part": "You will never be famous"}
###
Message: I can't run a marathon, but I wish I could
{"sad_part": "You can't run a marathon"}
###
Message: You are as tall as you will ever be and I guess it is too bad
{"sad_part": "You are as tall as you will ever be"}
###
Message: It is such a bummer that dogs don't live as long as people
{"sad_part": "Dogs don't live as long as people"}
###
Message: I may never be able to go to the moon and it makes me sad
{"sad_part": "You may never be able to go to the moon"}
###
Message: Finding a swe internship is challenging.
{"sad_part": "You may never find a SWE internship"}
###
'''
    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['sad_part'], 20)

            d.text((425, 500), wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((50, 1300), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name
