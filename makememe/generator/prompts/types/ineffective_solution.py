from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Ineffective_Solution(Prompt):
    name = "Ineffective_Solution"
    description = "ineffective solution"

    def __init__(self):
        self.instruction = '''
###
Message: There is a bunch of traffic in town. The government decided to make the roads wider, but that's not the problem
Meme:{"attempted_solution":"more roads", "failure":"traffic"}
###
Message: Some people who brush their hair still get messy hair.
Meme:{"attempted_solution":"brush", "failure":"messy hair"}
###
Message: I go for a walk daily, but then I end up eating a donut. Pretty ineffective
Meme:{"attempted_solution":"walk daily", "failure":"eating a donut"}
###
Message: I drink coffee to be more awake, but then I can't sleep and I am tired the next day
Meme:{"attempted_solution":"drink coffee", "failure":"can't sleep and I am tired the next day"}
###
Message: I try to read a book to spend less time on my phone, but I end up googling concepts on my phone
Meme:{"attempted_solution":"read a book to spend less time on my phone", "failure":"end up googling concepts on my phone"}
###
Message: bralkajsd;
Meme:{"attempted_solution":"bralkajsd;", "failure":"bralkajsd;"}
###
Message: I wish AI could help me make memes
Meme:{"attempted_solution":"AI making memes", "failure":"The memes are beyond my sense of humor"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['attempted_solution'], position=(75, 75), font_size=50, text_color="white", wrapped_width=14)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['failure'], position=(125, 725), font_size=50, text_color="white", wrapped_width=15, rotate_degrees=350)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(20, 1150), font_size=25, text_color="white")
           
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

