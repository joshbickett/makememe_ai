from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont, ImageOps
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class In_My_Opinion(Prompt):
    name = "In_My_Opinion"
    description = "in my opinion"

    def __init__(self):
        self.instruction = '''
###
Message: Running a marathon is a great accomplishment and I don't care what anyone says.
{"opinion":"Running a marathon is a great accomplishment"}
###
Message: Learning to code is the best for your career
{"opinion":"Learning to code is the best for your career"}
###
Message: Daft Punk is the greatest electronic band to ever exist and you can't convince me otherwise
{"opinion":"Daft Punk is the greatest electronic band to ever exist"}
###
Message: Breakfast is an unnecessary meal. Change my mind
{"opinion":"Breakfast is an unnecessary meal. "}
###
Message: Please should not allow their dogs to over eat
{"opinion":"Please should not allow their dogs to over eat"}
###
Message: Controlled fire burns are the best way to do forest management
{"opinion":"Controlled fire burns are the best way to do forest management"}
###
Message: It appears to me we need to go outside more often and we'll be happier
{"opinion":"we need to go outside more often and we'll be happier"}
###
Message: If only we were more kind to each other, this world would be a more pleasant place.
{"opinion":"If only we were more kind to each other, this world would be a more pleasant place."}
###
'''

    def create(self, meme_text):
        # with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

        base=Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg")

        wrapped_text = Helper.wrap(meme_text['opinion'], 25)

        font = ImageFont.truetype(font_path, 25)
        txt=Image.new('L', (500,50))
        d = ImageDraw.Draw(txt)
        d.text( (0, 0), wrapped_text,  font=font, fill=255)
        w=txt.rotate(20,  expand=1)

        base.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (600,360),  w)

        date = datetime.datetime.now()
        image_name = f'{date}.jpg'
        file_location = f'makememe/static/creations/{image_name}'
        base.save(file_location)
        return image_name


        # font = ImageFont.truetype(font_path, 25)
        # watermark_font = ImageFont.truetype(font_path, 15)
        # d = ImageDraw.Draw(txt)

        
        

        # d.text((600, 360),wrapped_text, font=font, fill=(0, 0, 0, 255))
        # d.text((10, 500), "makememe.ai", font=watermark_font, fill=(255, 255, 255, 128))
        
        # w = txt.rotate(17.5, expand=1)
        # # out = Image.alpha_composite(base, w)
        # base.paste(w)
        # if base.mode in ("RGBA", "P"):
        #     base = base.convert("RGB")
        

