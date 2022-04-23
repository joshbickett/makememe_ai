from makememe.generator.prompts.prompt import Prompt
import datetime
from PIL import Image
from makememe.generator.design.image_manager import Image_Manager


class Stay_Away_From(Prompt):
    name = "Stay_Away_From"
    description = "stay away from"

    def __init__(self):
        self.instruction = """
###
Message:I typically prefer to stay away from people who are not my friends.
Meme:{"subject":"who are not my friends."}
###
Message:I don't hang out with Tiktokers
Meme:{"subject":"Tiktokers"}
###
"""

    def create(self, meme_text):
        with Image.open(f"makememe/static/meme_pics/{self.name.lower()}.jpg").convert(
            "RGBA"
        ) as base:

            overlay_image = Image_Manager.add_text(
                base=base,
                text=meme_text["subject"],
                position=(115, 300),
                font_size=30,
                wrapped_width=15,
            )
            watermark = Image_Manager.add_text(
                base=base, text="makememe.ai", position=(10, 475), font_size=8
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
