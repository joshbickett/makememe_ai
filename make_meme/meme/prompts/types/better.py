from meme.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from meme.prompts.helper import Helper


class Better(Prompt):
    def __init__(self):
        self.instruction = '''
"I like coffee, but tea is much better" 
{"worse":"coffee", "better":"tea"}
###
"Dr. Dre is nothing compared to Kanye" 
{"worse":"Dr. Dre", "better":"Kanye"}
###
"I don't want a Honda, I want a Tesla" 
{"worse":"Honda", "better":"Tesla"}
###
"We don't need a new car, we need a new robot"
{"worse":"new car", "better":"new robot"}
###
"Facebook is no good compared to Twitter"
{"worse":"Facebook", "better":"Twitter"}
###
"Dogs make you happy while cats make you sad"
{"worse":"cats", "better":"dogs"}
###
"I love apples, while I don't care so much for oranges"
{"worse":"oranges","better":"apples"}
###
"Daft punk is the greatest, while U2 is not that good"
{"worse":"u2","better":"daft punk"}
###
"Riding a bike on dirt is more fun than writing a bike on the street"
{"worse":"writing a bike on the street","better":"riding a bike on dirt"}
###
"Surfing in warm water is more enjoyable than surfing in cold water"
{"worse":"surfing in cold water","better":"surfing in warm water"}
###
"Spending time on the internet to make people laugh is better then doing it to cause outrage"
{"worse":"Spending time on the internet to cause outrage","better":"Spending time on the internet to making people laugh"}
###
'''

    def create(self, meme_text):
        with Image.open("meme/static/meme_pics/better.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            fnt = ImageFont.truetype("Keyboard.ttf",50)
            d = ImageDraw.Draw(txt)

            better_meme_text = Helper.wrap(meme_text['better'].replace("'", ""), 15)
            worse_meme_text = Helper.wrap(meme_text['worse'].replace("'", ""), 15)

            d.text((625, 200), worse_meme_text, font=fnt, fill=(0, 0, 0, 128))
            d.text((625, 600), better_meme_text, font=fnt, fill=(0, 0, 0, 128))
            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'meme/static/creations/{image_name}'
                out.save(file_location)
                return image_name

