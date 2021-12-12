from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Dont_Care(Prompt):
    name = "Dont_Care"
    description = "don't care"

    def __init__(self):
        self.instruction = '''
###
Message: Doesn't matter to me that facebook is buying oculus
{"action":"Facebook buying oculus"}
###
Message: I dislike going running, it is so much work.
{"action":"Going running"}
###
Message: Doing laundry is the worst, I really don't care for it
{"action":"Doing laundry"}
###
Message: Some people cut in line and don't care about others
{"action":""people cut in line"}
###
Message: We should all wear sunscreen, but some people don't seem to care
{"action":"wearing sunscreen"}
###
Message: Getting patents is sometimes important, but sometimes it is not at all
{"action":"Getting patents is sometimes important"}
###
Message: Make sure to always writing test before writing code
{"action":"Make sure to always writing test before writing code"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['action'], position=(100, 175), font_size=40, wrapped_width=11)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(100, 1100), font_size=20)
            
            base = Image.alpha_composite(base, watermark)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

