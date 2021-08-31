from meme.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from meme.prompts.helper import Helper


class Cry(Prompt):
    def __init__(self):
        self.instruction = '''
"We still haven't been to Mars and it makes me cry" 
{"sad_part": "We still haven't been to Mars"}
###
"My college degree didn't get me a job and now I am in debt" 
{"sad_part": "Your college degree didn't get you a job and now you're in debt"}
###
"I have to actually read to learn something" 
{"sad_part": "You have to actually read to learn something"}
###
"I will never be famous and it's tragic" 
{"sad_part": "You will never be famous"}
###
"I can't run a marathon, but I wish I could" 
{"sad_part": "You can't run a marathon"}
###
"You are as tall as you will ever be and I guess it is too bad" 
{"sad_part": "You are as tall as you will ever be"}
###
"It is such a bummer that dogs don't live as long as people" 
{"sad_part": "Dogs don't live as long as people"}
###
"I may never be able to go to the moon and it makes me sad" 
{"sad_part": "You may never be able to go to the moon"}
###
'''
    def create(self, meme_text):
        with Image.open("meme/static/meme_pics/cry.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            fnt = ImageFont.truetype("Keyboard.ttf",40)
            d = ImageDraw.Draw(txt)

            meme_text_wrapped = Helper.wrap(meme_text['sad_part'].replace("'", ""), 20)

            d.text((425, 500), meme_text_wrapped, font=fnt, fill=(0, 0, 0, 255))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'meme/static/creations/{image_name}'
                out.save(file_location)
                return image_name
