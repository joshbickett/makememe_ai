from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Better_And_Distracting(Prompt):
    name = "Better_And_Distracting"
    description = 'better and distracting'

    def __init__(self):
        self.instruction = '''
###
Message: I am working on new side project and now my old projects are neglected.
{"neglected":"new side project", "subject":"me", "distraction":"my old projects"}
###
Message: My friends never want to watch movies on Netflix. Instead they just watch Youtube all the time.
{"neglected":"watch movies on Netflix", "subject":"My friends", "distraction":"watch Youtube"}
###
Message: I can't help but listening to the new Daft Punk album and stop listening to Radiohead for now
{"neglected":"listening to Radiohead", "subject":"me", "distraction":"Listening to the new Daft Punk album"}
###
Message: Programmer tend to use if functions instead of thinking out the switch statement
{"neglected":"thinking out the switch statement", "subject":"Programmer", "distraction":"use if functions"}
###
Message: I am creating a AI algorithm, but now I am getting distracted by creating a NFT
{"neglected":"creating a AI algorithm", "subject":"me", "distraction":"creating a NFT"}
###
Message: I get distracted by job postings because I am freelancing all the time.
{"neglected":"freelancing", "subject":"me", "distraction":"job postings"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path, 40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)

            meme_text_one = Helper.wrap(meme_text['neglected'], 15)
            meme_text_two = Helper.wrap(meme_text['subject'], 15)
            meme_text_three = Helper.wrap(meme_text['distraction'], 15)

            d.text((115, 100), meme_text_one, font=font, fill=(0, 0, 0, 255))
            d.text((650, 100), meme_text_two, font=font, fill=(0, 0, 0, 255))
            d.text((800, 100), meme_text_three, font=font, fill=(0, 0, 0, 255))
            d.text((10, 800), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))

            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

