from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Better(Prompt):
    name = "Better"
    description = "better"

    def __init__(self):
        self.instruction = '''
###
Message: I like coffee, but tea is much better
{"worse":"coffee", "better":"tea"}
###
Message: Dr. Dre is nothing compared to Kanye
{"worse":"Dr. Dre", "better":"Kanye"}
###
Message: I don't want a Honda, I want a Tesla
{"worse":"Honda", "better":"Tesla"}
###
Message: We don't need a new car, we need a new robot
{"worse":"new car", "better":"new robot"}
###
Message: Facebook is no good compared to Twitter
{"worse":"Facebook", "better":"Twitter"}
###
Message: Dogs make you happy while cats make you sad
{"worse":"cats", "better":"dogs"}
###
Message: I love apples, while I don't care so much for oranges
{"worse":"oranges","better":"apples"}
###
Message: Daft punk is the greatest, while U2 is not that good
{"worse":"u2","better":"daft punk"}
###
Message: Tim and Grace are not friends yet
{"worse":"Tim","better":"Grace"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,50)
            watermark_font = ImageFont.truetype(font_path,25)
            d = ImageDraw.Draw(txt)

            better_meme_text = Helper.wrap(meme_text['better'], 15)
            worse_meme_text = Helper.wrap(meme_text['worse'], 15)

            d.text((100, 700), better_meme_text, font=font, fill=(255, 255, 255, 255))
            d.text((400, 700), worse_meme_text, font=font, fill=(255, 255, 255, 255))
            d.text((10, 1300), "makememe.ai", font=watermark_font, fill=(255, 255, 255, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name


