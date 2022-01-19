from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Pompous(Prompt):
    name = "Pompous"
    description = "pompous"

    def __init__(self):
        self.instruction = '''
###
Message: People who run marathon think they are superior. Maybe that's the case
Meme:{"subject":"Running marathon"}
###
Message: People who play chess seem to think they are better than people who play checkers
Meme:{"subject":"People who play chess"}
###
Message: Coding gives people a feeling of being great
Meme:{"subject":"Coding"}
###
Message: Shareholders that don't have to report to any managers and make money think it is great.
Meme:{"subject":"Not reporting to any managers"}
###
Message: Being able to do a front flip makes people pompus
Meme:{"subject":"Being able to do a front flip"}
###
Message: That was fun, but now I need to learn how to ride a bicycle
Meme:{"subject":"Riding sa bicycle"}
###
Message: Using a drip coffee system works, but have you tried using a french press??
Meme:{"subject":"using a french press"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['subject'], position=(30, 900), font_size=40, wrapped_width=10)

            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(30, 1125), font_size=20)
            
            base = Image.alpha_composite(base, watermark)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name

