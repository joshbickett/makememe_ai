from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path

class Poor_Fix(Prompt):
    name = "Poor_Fix"
    description = "poor fix"

    def __init__(self):
        self.instruction = '''
###
Message: They government thinks it can print more money and it will solve our problems
{"subject":"government", "action":"print more money"} 
###
Message: Startups will hire more software engineers and think it will fix everything
{"subject":"startups", "action":"hire more software engineers"} 
###
Message: Unproductive people will drink more coffee thinking that will make their work get done
{"subject":"Unproductive people", "action":"drink more coffee"} 
###
Message: Stressed people will go for a run to help them feel better
{"subject":"Stressed people", "action":"go for a run"} 
###
Message: The government built a road when we needed a rail way
{"subject":"government", "action":"built a road"} 
###
'''
    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            font = ImageFont.truetype(font_path,60)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)
            d.text((200, 200), meme_text['subject'], font=font, fill=(255, 255, 255, 255))
            d.text((200, 800), meme_text['action'], font = font, fill = (255, 255, 255, 255))
            d.text((10, 1200), "makememe.ai", font=watermark_font, fill=(255, 255, 255, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

