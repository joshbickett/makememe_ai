from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Accurate_Depiction(Prompt):
    name = "Accurate_Depiction"
    description = "accurate depiction"

    def __init__(self):
        self.instruction = '''
###
Message: They told me I am too interested in crypto currencies and they couldn't be more right
{"depiction":"You are too interested in crypto currencies"}
###
Message: I had a fortune cookie tell me I code too much and It is so correct.
{"depiction":"You code too much"}
###
Message: You want to hear an accurate depiction. I am not running enough.
{"depiction":"You are not running enough"}
###
Message: They don't go outside enough. They need to get some sunlight. It's the truth
{"depiction":"They need to go outside more"}
###
Message: Humans making memes ok, AI making memes awesome.
{"depiction":"You want AI making memes"}
###
'''

    def create(self, meme_text):
            base=Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg")

            Image_Manager.add_text(base=base, text="makememe.ai", position=(10, 1150), font_size=20, text_color="black", wrapped_width=None, rotate_degrees=None)
            Image_Manager.add_text(base=base, text=meme_text['depiction'], position=(250, 725), font_size=30, text_color="black", text_width_proportion=2, wrapped_width=25, rotate_degrees=348)

            date = datetime.datetime.now()
            image_name = f'{date}.jpg'
            file_location = f'makememe/static/creations/{image_name}'
            base.save(file_location)
            return image_name

