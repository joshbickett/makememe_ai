from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Change_My_Mind(Prompt):
    name = "Change_My_Mind"
    description = "This is my opinion. Change my mind."

    def __init__(self):
        self.instruction = '''
###
Message:Chocolate chip cookies are the best cookies. Try to change my mind.
Meme:{"opinion":" Chocolate chip cookies are the best cookies. Change my mind."}
###
Message:Learning to code is one of the most rewarding experiences. Change my mind.
Meme:{"opinion":"Learning to code is one of the most rewarding experiences. Change my mind."}
###
Message:Daft Punk is the greatest electronic band to ever exist and you can't convince me otherwise.
Meme:{"opinion":"Daft Punk is the greatest electronic band to ever exist. Change my mind."}
###
Message:In my opinion, the best way to get a good grade in school is to study hard.
Meme:{"opinion":"The best way to get a good grade in school is to study hard.. Change my mind."}
###
'''

    def create(self, meme_text):

        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['opinion'], position=(190,200), font_size=60, text_color="black", wrapped_width=22)
            watermark = Image_Manager.add_text(base=base, text="makememe.ai", position=(25,900), font_size=25, text_color="white")

            base = Image.alpha_composite(base, watermark)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f'{date}.jpg'
                file_location = f'makememe/static/creations/{image_name}'
                out.save(file_location)
                return image_name
    

