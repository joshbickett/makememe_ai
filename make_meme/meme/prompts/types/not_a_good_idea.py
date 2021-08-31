from meme.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from meme.prompts.helper import Helper


class Not_A_Good_Idea(Prompt):
    def __init__(self):
        self.instruction = '''
"Facebook buying oculus" 
{"problem":"Facebook buying oculus"}
###
"I hate going running, it is so much work." 
{"problem":"Going running"}
###
"I hate going running, it is so much work." 
{"problem":"Going running"}
###
"Doing laundry is the worst, I hate it" 
{"problem":"Doing laundry"}
###
"Cutting in line is the worst" 
{"problem":""Cutting in line"}
###
'''

    def create(self, meme_text):
        with Image.open("meme/static/meme_pics/not_a_good_idea.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            fnt = ImageFont.truetype("Keyboard.ttf", 40)
            d = ImageDraw.Draw(txt)

            better_meme_text = Helper.wrap(meme_text['problem'].replace("'", ""), 15)

            d.text((100, 175),better_meme_text, font=fnt, fill=(0, 0, 0, 255))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'meme/static/creations/{image_name}'
                out.save(file_location)
                return image_name

