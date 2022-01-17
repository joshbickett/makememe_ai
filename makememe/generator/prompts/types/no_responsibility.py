from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class No_Responsibility(Prompt):
    name = "No_Responsibility"
    description = "no responsibility"

    def __init__(self):
        self.instruction = '''
###
Message: Company 1 is suing company 2 and neither thinks they are wrong
Meme:{"party_one":"Company 1", "party_two":"company 2"}
###
Message: The shoemaker blames the sockmaker and the sockmaker blames the shoemaker
Meme:{"party_one":"shoemaker", "party_two":"sockmaker"}
###
Message: Coffee blames tea for not waking me up after I drink both
Meme:{"party_one":"coffee blaming tea for not walking me up", "party_two":"tea"}
###
Message: I can't do anything useful
Meme:{"party_one":"me", "party_two":"me"}
###
Message: break
Meme:{"party_one":"break", "party_two":"break"}
###
Message: tlest;laksd
Meme:{"party_one":"test;laksd", "party_two":"test;laksd"}
###
Message: The code I wrote this week blames the code I wrote last week
Meme:{"party_one":"The code I wrote this week", "party_two":"the code I wrote last week"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['party_one'], position=(175, 200), font_size=50, text_color="white", wrapped_width=8)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['party_two'], position=(800, 200), font_size=50, text_color="white", wrapped_width=8)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(10, 515), font_size=25, text_color="white")
        
            base = Image.alpha_composite(base, watermark)
            base = Image.alpha_composite(base, overlay_image_2)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name


