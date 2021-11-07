from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class No_Responsibility(Prompt):
    name = "No_Responsibility"
    description = "no responsibility"

    def __init__(self):
        self.instruction = '''
###
Message: The federal government blames the state government and no group takes responsibility
{"party_one":"federal government", "party_two":"state government"}
###
Message: Company 1 is suing company 2 and neither thinks they are wrong
{"party_one":"Company 1", "party_two":"company 2"}
###
Message: The shoemaker blames the sockmaker and the sockmaker blames the shoemaker
{"party_one":"shoemaker", "party_two":"sockmaker"}
###
Message: Mom sometimes blames dad for not taking out the trash, but dad blames mom who leaves too much trash.
{"party_one":"dad for not taking out the trash", "party_two":"mom who leaves too much trash."}
###
Message: Coffee blames tea for not waking me up after I drink both
{"party_one":"coffee blaming tea for not walking me up", "party_two":"tea"}
###
Message: I can't do anything useful
{"party_one":"me", "party_two":"me"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,50)
            watermark_font = ImageFont.truetype(font_path, 25)
            d = ImageDraw.Draw(txt)

            meme_text_one = Helper.wrap(meme_text['party_one'], 15)
            meme_text_two = Helper.wrap(meme_text['party_two'], 15)

            d.text((100, 200), meme_text_one, font=font, fill=(255, 255, 255, 255))
            d.text((700, 200), meme_text_two, font=font, fill=(255, 255, 255, 255))
            d.text((10, 515), "makememe.ai", font=watermark_font, fill=(255, 255, 255, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name


