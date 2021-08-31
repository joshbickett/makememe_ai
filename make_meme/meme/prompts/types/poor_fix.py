from meme.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from meme.prompts.helper import Helper

class Poor_Fix(Prompt):
    def __init__(self):
        self.instruction = '''
"They government thinks it can print more money and it will solve our problems"
{"subject":"government", "poor fix":"print more money"} 
###
"Startups will hire more software engineers and think it will fix everything"
{"subject":"startups", "poor fix":"hire more software engineers"} 
###
"Unproductive people will drink more coffee thinking that will make their work get done"
{"subject":"Unproductive people", "poor fix":"drink more coffee"} 
###
"Stressed people will go for a run to help them feel better"
{"subject":"Stressed people", "poor fix":"go for a run"} 
###
'''
    def create(self, meme_text):
        with Image.open("meme/static/meme_pics/poor_fix.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            fnt = ImageFont.truetype("Keyboard.ttf",60)
            d = ImageDraw.Draw(txt)
            d.text((200, 200), meme_text['subject'], font=fnt, fill=(255, 255, 255, 255))
            d.text((200, 800), meme_text['poor fix'], font = fnt, fill = (255, 255, 255, 255))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'meme/static/creations/{image_name}'
                out.save(file_location)
                return image_name

