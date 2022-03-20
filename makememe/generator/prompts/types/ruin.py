from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Ruin(Prompt):
    name = "Ruin"
    description = "ruin"

    def __init__(self):
        self.instruction = '''
###
Message:Me getting a good at a library is ruined by a new library replacing it.
Meme:{"subject":"Me getting good at a new library", "ruiner":"new library replacing it"}
###
Message:When you're halfway through a book, but can't finish it because a new TV show you love comes out
Meme:{"subject":"halfway through a book", "ruiner":"new TV show you love comes out"}
###
Message:Apple Music really can't keep up with Spotify's innovation
Meme:{"subject":"Apple Music", "ruiner":"Spotify's innovation"}
###
Message:a
Meme:{"subject":"a", "ruiner":" "}
###
Message:Getting rid of an accumulation of stuff I don't use is ruined by Christmas gifts
Meme:{"subject":"Getting rid of an accumulation of stuff I don't use", "ruiner":"Christmas gifts"}
###
Message:Hodle
Meme:{"subject":"Hodle", "ruiner":"Hodle"}
###
'''

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert("RGBA") as base:

            overlay_image = Image_Manager.add_text(base=base, text=meme_text['subject'], position=(400, 25), font_size=50, text_color="white", wrapped_width=20)
            overlay_image_2 = Image_Manager.add_text(base=base, text=meme_text['ruiner'], position=(120, 915), font_size=50, text_color="white", wrapped_width=12)
            watermark = Image_Manager.add_text(base=base, text='makememe.ai', position=(10, 1175), font_size=25, text_color="white")
        
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


