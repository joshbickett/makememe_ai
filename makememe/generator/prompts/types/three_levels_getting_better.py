from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Three_Levels_Getting_Better(Prompt):
    name = "Three_Levels_Getting_Better"
    description = 'three levels getting better'

    def __init__(self):
        self.instruction = '''
###
Message: This is somewhat exciting, that is more exciting, but THAT IS extremely exciting
{"somewhat exciting":"this", "more exciting":"that", "extremely exciting":"THAT"}
###
Message: Apples are cool, pears are very cool, but pineapples are the best
{"somewhat exciting":"apples", "more exciting":"pears", "extremely exciting":"pineapples"}
###
Message: Going for a walk is nice and going for a jog is pretty good. Nothing is as good as running though!
{"somewhat exciting":"going for a walk", "more exciting":"going for a jog", "extremely exciting":"going for a run"}
###
Message: Nothing is as cool as learning to code. Reading HTML is cool and learning about computers is ok.
{"somewhat exciting":"learning about computers", "more exciting":"reading HTML", "extremely exciting":"learning to code"}
###
Message: Option 1 is somewhat exciting. Option 2 is more exciting. Option 3 is extremely exciting
{"somewhat exciting":"Option 1", "more exciting":"Option 2", "extremely exciting":"Option 3"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            somewhat_text = Helper.wrap(meme_text['somewhat exciting'], 25)
            more_text = Helper.wrap(meme_text['more exciting'], 25)
            extremely_text = Helper.wrap(meme_text['extremely exciting'], 25)

            d.text((25, 100), somewhat_text, font=font, fill=(0, 0, 0, 255))
            d.text((25, 475), more_text, font=font, fill=(0, 0, 0, 255))
            d.text((25, 875), extremely_text, font=font, fill=(0, 0, 0, 255))
            d.text((25, 1100), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))

            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

