from meme.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from meme.prompts.helper import Helper

class They_Dont_Know(Prompt):
    def __init__(self):
        self.instruction = '''
"I am so proud of my new website that sells dog treats"
{"meme":"They don't know I have a new website that sells dog treats"} 
###
"They don't know I started a company"
{"meme":"They don't know I started a company"} 
###
"Everyone would be impressed that I can run a marathon"
{"meme":"They don't know I can run a marathon"} 
###
"No one cares that I am getting married this month"
{"meme":"They don't know that I am getting married this month"} 
###
"They don't know that I have a lot of followers on Twitter"
{"meme":"They don't know that I have a lot of followers on Twitter"} 
###
"We don't care that you have a masters in computer science"
{"meme":"They don't know that I have a masters in computer science"} 
###
"People think it's so important that they can do social media marketing"
{"meme":"They don't know that I can do social media marketing"} 
###
'''
    def create(self, meme_text):
        with Image.open("meme/static/meme_pics/they_dont_know.png").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            fnt = ImageFont.truetype("Keyboard.ttf",40)
            d = ImageDraw.Draw(txt)
            better_meme_text = Helper.wrap(meme_text['meme'].replace("'", ""), 15)


            d.text((400, 100), better_meme_text, font = fnt, fill = (0, 0, 0, 255))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'meme/static/creations/{image_name}'
                out.save(file_location)
                return image_name
