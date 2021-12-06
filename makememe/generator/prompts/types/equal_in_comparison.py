from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class Equal_In_Comparison(Prompt):
    name = "Equal_In_Comparison"
    description = "equal in comparison"

    def __init__(self):
        self.instruction = '''
###
Message: Tea and coffee are equally is good. They both make me happy
{"first":"Tea", "second":"coffee"}
###
Message: Both Dr. Dre and Kanye are amazing. I love them both
{"first":"Dr. Dre", "second":"Kanye"}
###
Message: If I had to decide between Honda and Tesla I couldn't. They are both great.
{"first":"Honda", "second":"Tesla"}
###
Message: Riding a bike on dirt is just as fun as riding on the street
{"first":"writing a bike on the dirt","second":"writing a bike on the street"}
###
Message: Surfing in warm water is the same as surfing in cold water. They are equally fun
{"first":"surfing in cold water","second":"surfing in warm water"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,50)
            watermark_font = ImageFont.truetype(font_path, 25)
            d = ImageDraw.Draw(txt)

            meme_text_one = Helper.wrap(meme_text['first'], 15)
            meme_text_two = Helper.wrap(meme_text['second'], 15)

            d.text((150, 200), meme_text_one, font=font, fill=(0, 0, 0, 255))
            d.text((600, 250), meme_text_two, font=font, fill=(0, 0, 0, 255))
            d.text((10, 1300), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name


