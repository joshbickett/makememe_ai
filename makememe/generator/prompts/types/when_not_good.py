from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class When_Not_Good(Prompt):
    name = "When_Not_Good"
    description = "when something is really bad"

    def __init__(self):
        self.instruction = """
###
Message:When all your friends are getting married and you've not been on a date.
Meme:{"subject": "When all your friends are getting married and you've not been on a date."}
###
Message:I got a 4 year engineering degree and now can't remember calculus.
Meme:{"subject": "When you get a 4 year engineering degree and now can't remember calculus."}
###
Message:It's not good that this new strain is spreading fast
Meme:{"subject": "When the new strain is spreading fast"}
###
Message:When I have to run a full marathon, but I haven't trained for it.
Meme:{"subject": "When I have to run a full marathon, but I haven't trained for it."}
###
"""

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["subject"],
                position=(100, 50),
                font_size=45,
                wrapped_width=40,
            )
            watermark = Image_Manager.add_text(
                base=base, text="makememe.ai", position=(10, 800), font_size=20
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
