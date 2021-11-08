from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Not_Good(Prompt):
    name = "Not_Good"
    description = "not good"

    def __init__(self):
        self.instruction = '''
###
Message: It appears a waste to me that facebook is buying oculus
{"not_good":"Facebook is buying oculus"}
###
Message: Blue Origin is suing Nasa instead of working with them. How lame.
{"not_good":"Blue Origin is sueing Nasa"}
###
Message: I had to walk in the smoke because there was a fire
{"not_good":"walking in the smoke"}
###
Message: Programmer tend to use if functions instead of thinking out the switch statement
{"not_good":"Thinking out the switch statement"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            wrapped_text = Helper.wrap(meme_text['not_good'], 15)

            d.text((300, 800),wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((10, 1100), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

