from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager

class Completes(Prompt):
    name = "Completes"
    description = "completes"

    def __init__(self):
        self.instruction = '''
###
Message: A good dessert makes me so happy
Meme:{"pieces that completes": "a good desert"}
###
Message: I feel so completed after a long run outside
Meme:{"pieces that completes": "long run outside"}
###
'''
    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['pieces that completes'], position=(700, 425), font_size=45, wrapped_width=12)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(850, 1150), font_size=20)

            base = Image.alpha_composite(base, watermark)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name
