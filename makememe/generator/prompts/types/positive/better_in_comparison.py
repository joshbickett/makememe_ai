from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Better_In_Comparison(Prompt):
    name = "Better_In_Comparison"
    description = "better in comparison"

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
Message: Riding a bike on dirt is more fun than writing a bike on the street
{"worse":"writing a bike on the street","better":"riding a bike on dirt"}
###
Message: Surfing in warm water is more enjoyable than surfing in cold water
{"worse":"surfing in cold water","better":"surfing in warm water"}
###
Message: Spending time on the internet to make people laugh is better then doing it to cause outrage
{"worse":"Spending time on the internet to cause outrage","better":"Spending time on the internet to making people laugh"}
###
Message: Humans making memes ok, AI making memes awesome.
{"worse":"human making memes","better":"AI making memes"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,50)
            watermark_font = ImageFont.truetype(font_path, 35)
            d = ImageDraw.Draw(txt)

            meme_text_one = Helper.wrap(meme_text['better'], 15)
            meme_text_two = Helper.wrap(meme_text['worse'], 15)

            d.text((625, 100), meme_text_two, font=font, fill=(0, 0, 0, 128))
            d.text((625, 525), meme_text_one, font=font, fill=(0, 0, 0, 128))
            d.text((800, 1000), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name


