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
        print("meme text in class: ", meme_text)

        base=Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg")

        wrapped_text = Helper.wrap(meme_text['opinion'], 25)

        meme_font = ImageFont.truetype(font_path, 25)
        watermark_font = ImageFont.truetype(font_path, 25)

        meme_text_overlay =Image.new('L', (int(base.width/4), int(base.height/4)), 0)
        meme_draw = ImageDraw.Draw(meme_text_overlay)
        meme_draw.text((0, 0), wrapped_text,  font=meme_font, fill=255)
        meme_text_overlay=meme_text_overlay.rotate(20,  expand=1)

        watermark_overlay =Image.new('L', (int(base.width/4), int(base.height/4)), 0)
        watermark_draw = ImageDraw.Draw(watermark_overlay)
        watermark_draw.text((0, 0), "makememe.ai",  font=watermark_font, fill=255)
        base.paste(ImageOps.colorize(meme_text_overlay, (0,0,0), (0,0,0)), (575,300), meme_text_overlay)
        base.paste(ImageOps.colorize(watermark_overlay, (0,0,0), (255,255,255)), (25,600), watermark_overlay)

        date = datetime.datetime.now()
        image_name = f'{date}.jpg'
        file_location = f'makememe/static/creations/{image_name}'
        base.save(file_location)
        return image_name
        return 'test'
        

