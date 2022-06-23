from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Indifferent(Prompt):
    id = 2
    name = "Indifferent"
    description = "this is not important to me"

    def __init__(self):
        self.instruction = """
###
Message:Doesn't matter to me that facebook is buying oculus
Meme:{"action":"Facebook buying oculus"}
###
Message:I dislike going running, it is so much work.
Meme:{"action":"Going running"}
###
Message:Doing laundry is the worst, I really don't care for it
Meme:{"action":"Doing laundry"}
###
Message:Some people cut in line and don't care about others
Meme:{"action":"people cut in line"}
###
Message:We should all wear sunscreen, but some people don't seem to care
Meme:{"action":"wearing sunscreen"}
###
Message:Getting patents is sometimes important, but sometimes it is not at all
Meme:{"action":"Getting patents is sometimes important"}
###
Message:Make sure to always writing test before writing code
Meme:{"action":"Make sure to always writing test before writing code"}
###
Message:Break
Meme:{"action":"Break"}
###
Message:I wish I could go to the moonb
Meme:{"action":"going to the moon"}
###
"""

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["action"],
                position=(100, 175),
                font_size=40,
                wrapped_width=11,
            )
            watermark = Image_Manager.add_text(
                base=base, text="makememe.ai", position=(100, 1100), font_size=20
            )

            base = Image.alpha_composite(base, watermark)
            out = Image.alpha_composite(base, overlay_image)
            if out.mode in ("RGBA", "P"):
                out = out.convert("RGB")
                date = datetime.datetime.now()
                image_name = f"{date}.jpg"
                file_location = f"makememe/static/creations/{image_name}"
                out.save(file_location)
                return image_name
