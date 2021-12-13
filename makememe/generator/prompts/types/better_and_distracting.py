from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.image_manager import Image_Manager


class Better_And_Distracting(Prompt):
    name = "Better_And_Distracting"
    description = 'better and distracting'

    def __init__(self):
        self.instruction = '''
###
Message: I am working on new side project and now my old projects are neglected.
{"neglected":"new side project", "subject":"me", "distraction":"my old projects"}
###
Message: My friends never want to watch movies on Netflix. Instead they just watch Youtube all the time.
{"neglected":"watch movies on Netflix", "subject":"My friends", "distraction":"watch Youtube"}
###
Message: I can't help but listening to the new Daft Punk album and stop listening to Radiohead for now
{"neglected":"listening to Radiohead", "subject":"me", "distraction":"Listening to the new Daft Punk album"}
###
Message: Programmer tend to use if functions instead of thinking out the switch statement
{"neglected":"thinking out the switch statement", "subject":"Programmer", "distraction":"use if functions"}
###
Message: I am creating a AI algorithm, but now I am getting distracted by creating a NFT
{"neglected":"creating a AI algorithm", "subject":"me", "distraction":"creating a NFT"}
###
Message: I get distracted by job postings because I am freelancing all the time.
{"neglected":"freelancing", "subject":"me", "distraction":"job postings"}
###
Message: Try to break 
{"neglected":"break", "subject":"break","distraction":"break"}
###
Message: asd;lfkjasdf
{"neglected":"asd;lfkjasdf", "subject":"asd;lfkjasdf","distraction":"asd;lfkjasdf"}
###
Message: I want to learn web 3 but I am working on ai
{"neglected":"web 3", "subject":"me","distraction":"web 3"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['neglected'], position=(75, 75), font_size=45, wrapped_width=12)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['subject'], position=(470, 75), font_size=45, wrapped_width=12)
            overlay_image_3 = Image_Manager.add_text(base=base, text=meme_text['subject'], position=(850, 75), font_size=45, wrapped_width=12)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(10, 8000), font_size=20)

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

