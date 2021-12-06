from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class In_My_Opinion(Prompt):
    name = "In_My_Opinion"
    description = "in my opinion"

    def __init__(self):
        self.instruction = '''
###
Message: Running a marathon is a great accomplishment and I don't care what anyone says.
{"opinion":"Running a marathon is a great accomplishment"}
###
Message: Learning to code is the best for your career
{"opinion":"Learning to code is the best for your career"}
###
Message: Daft Punk is the greatest electronic band to ever exist and you can't convince me otherwise
{"opinion":"Daft Punk is the greatest electronic band to ever exist"}
###
Message: Breakfast is an unnecessary meal. Change my mind
{"opinion":"Breakfast is an unnecessary meal. "}
###
Message: Please should not allow their dogs to over eat
{"opinion":"Please should not allow their dogs to over eat"}
###
Message: Controlled fire burns are the best way to do forest management
{"opinion":"Controlled fire burns are the best way to do forest management"}
###
Message: It appears to me we need to go outside more often and we'll be happier
{"opinion":"we need to go outside more often and we'll be happier"}
###
Message: If only we were more kind to each other, this world would be a more pleasant place.
{"opinion":"If only we were more kind to each other, this world would be a more pleasant place."}
###
'''

    def create(self, meme_text):

        base=Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg")

        Image_Manager.add_text(base=base, text="makememe.ai", position=(25,600), font_size=25, text_color="white", wrapped_width=None, rotate_degrees=None)
        Image_Manager.add_text(base=base, text=meme_text['opinion'], position=(575,300), font_size=25, text_color="black", wrapped_width=25, rotate_degrees=20)

        date = datetime.datetime.now()
        image_name = f'{date}.jpg'
        file_location = f'makememe/static/creations/{image_name}'
        base.save(file_location)
        return image_name
        

