from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.image_manager import Image_Manager


class Three_Levels_Getting_Better(Prompt):
    name = "Three_Levels_Getting_Better"
    description = 'three levels getting better'

    def __init__(self):
        self.instruction = '''
###
Message: This is somewhat exciting, that is more exciting, but THAT IS extremely exciting
{"somewhat exciting":"this", "more exciting":"that", "extremely exciting":"THAT"}
###
Message: Apples are cool, pears are very cool, but pineapples are the best
{"somewhat exciting":"apples", "more exciting":"pears", "extremely exciting":"pineapples"}
###
Message: Going for a walk is nice and going for a jog is pretty good. Nothing is as good as running though!
{"somewhat exciting":"going for a walk", "more exciting":"going for a jog", "extremely exciting":"going for a run"}
###
Message: Nothing is as cool as learning to code. Reading HTML is cool and learning about computers is ok.
{"somewhat exciting":"learning about computers", "more exciting":"reading HTML", "extremely exciting":"learning to code"}
###
Message: Option 1 is somewhat exciting. Option 2 is more exciting. Option 3 is extremely exciting
{"somewhat exciting":"Option 1", "more exciting":"Option 2", "extremely exciting":"Option 3"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['somewhat exciting'], position=(25, 100), font_size=40, wrapped_width=18)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['more exciting'], position=(25, 475), font_size=40, wrapped_width=18)
            overlay_image_3 = Image_Manager.add_text(base=base, text=meme_text['extremely exciting'], position=(25, 875), font_size=40, wrapped_width=18)
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

