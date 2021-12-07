from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageChops
from makememe.generator.design.font import font_path
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.image_manager import Image_Manager


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

        # base=Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg")
        # Image_Manager.add_text(base=base, text="makememe.ai", position=(10, 1150), font_size=20, text_color="black", wrapped_width=None, rotate_degrees=None)
        # Image_Manager.add_text(base=base, text=meme_text['depiction'], position=(250, 725), font_size=30, text_color="black", text_width_proportion=2, wrapped_width=25, rotate_degrees=348)

        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            # txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            # font = ImageFont.truetype(font_path,50)
            # watermark_font = ImageFont.truetype(font_path, 25)
            # d = ImageDraw.Draw(txt)
            overlay_image = Image_Manager.add_text(base, meme_text['first'], (75, 200), 45, wrapped_width=15, rotate_degrees=350)
            overlay_image_2 = Image_Manager.add_text(base, meme_text['second'], (575, 225), 45, wrapped_width=15, rotate_degrees=350)

            base = Image.alpha_composite(base, overlay_image)
            out = Image.alpha_composite(base, overlay_image_2)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name


