from sqlalchemy.sql.expression import text
from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager

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
Message: as;dlfkja
{"subject":"as;dlfkja", "action":"as;dlfkja"} 
###
'''
    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['subject'], position=(125, 200), font_size=50, text_color="white", wrapped_width=15)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['action'], position=(350, 850), font_size=50, text_color="white", wrapped_width=20)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(50, 1250), font_size=30, text_color="black")
            
            base = Image.alpha_composite(base, watermark)
            base = Image.alpha_composite(base, overlay_image_2)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

