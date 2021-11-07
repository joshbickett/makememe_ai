from makememe.generator.prompts.prompt import Prompt
from PIL import Image, ImageDraw, ImageFont
import datetime
from makememe.generator.prompts.helper import Helper
from makememe.generator.design.font import font_path


class They_Dont_Know(Prompt):
    name = "They_Dont_Know"
    description = "they don't know"

    def __init__(self):
        self.instruction = '''
###
Message: I am so proud of my new website that sells dog treats
{"details":"They don't know I have a new website that sells dog treats"} 
###
Message: They don't know I started a company
{"details":"They don't know I started a company"} 
###
Message: Everyone would be impressed that I can run a marathon
{"details":"They don't know I can run a marathon"} 
###
Message: No one cares that I am getting married this month
{"details":"They don't know that I am getting married this month"} 
###
Message: They don't know that I have a lot of followers on Twitter
{"details":"They don't know that I have a lot of followers on Twitter"} 
###
Message: We don't care that you have a masters in computer science
{"details":"They don't know that I have a masters in computer science"} 
###
Message: "People think it's so important that they can do social media marketing
{"details":"They don't know that I can do social media marketing"} 
###
Message: I don't know if you guys realized I can an write an App in ReactJS while also using the Django framework on the backend
{"details":"They don't know that I can an write an App in ReactJS while also using the Django framework on the backend"}
###
'''
    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (0, 0, 0, 0))
            font = ImageFont.truetype(font_path,40)
            watermark_font = ImageFont.truetype(font_path, 20)
            d = ImageDraw.Draw(txt)
            wrapped_text = Helper.wrap(meme_text['details'], 15)

            d.text((400, 100), wrapped_text, font=font, fill=(0, 0, 0, 255))
            d.text((850, 1100), "makememe.ai", font=watermark_font, fill=(0, 0, 0, 255))

            out = Image.alpha_composite(base, txt)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                # User.objects.filter()
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name
