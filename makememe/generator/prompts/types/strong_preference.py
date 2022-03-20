from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Strong_Preference(Prompt):
    name = "Strong_Preference"
    description = 'The subject has a strong preference for one option over another'

    def __init__(self):
        self.instruction = '''
###
Message:Programmers prefer to use print statements over debug libraries
Meme:{"subject":"programmers", "less preferred":"print statements", "more preferred":"debug libraries"}
###
Message:I like running outside more than running in a Gym
Meme:{"subject":"runners", "less preferred":"running outside", "more preferred":"running in a gym"}
###
Message:I prefer this option greatly over that option
Meme:{"subject":"me", "less preferred":"running outside", "more preferred":"running in a gym"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['subject'], position=(500, 700), text_color="white", font_size=50, wrapped_width=18)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['less preferred'], position=(275, 200), text_color="white", font_size=50, wrapped_width=8)
            overlay_image_3 = Image_Manager.add_text(base=base, text=meme_text['more preferred'], position=(625, 200), text_color="white", font_size=50, wrapped_width=10)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(25, 1100), font_size=20, wrapped_width=18)
            
            base = Image.alpha_composite(base, watermark)
            base = Image.alpha_composite(base, overlay_image_2)
            base = Image.alpha_composite(base, overlay_image_3)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

