import os

from django.conf import settings
from django.contrib.staticfiles import finders
from django.utils.deconstruct import deconstructible

from PIL import Image, ImageDraw, ImageFont


@deconstructible
class FilePathProcessor:
    def __init__(self, path: str) -> None:
        self.path = path

    def __call__(self, instance, filename) -> str:
        ext = filename.split(".")[-1]
        filename = f"profile_image_user_{instance.user.id}.{ext}"
        return os.path.join(self.path, f"user_{instance.user.id}", filename)


class ImageGenerator:
    def __init__(
        self,
        font_size: int = 350,
        text_color: str = "#F5F5F5",
        background_color: str = "#111111",
    ):
        self.font_size = font_size
        self.text_color = text_color
        self.background_color = background_color

    def generate_image(self, instance) -> str:
        first_letter = instance.user.username[0].upper()
        image_size = (500, 500)
        image = Image.new("RGB", image_size, color=self.background_color)
        draw = ImageDraw.Draw(image)

        font_path = finders.find("fonts/kode_mono/KodeMono-SemiBold.ttf")

        try:
            font = ImageFont.truetype(font_path, self.font_size)
        except IOError:
            font = ImageFont.load_default()

        textbbox = draw.textbbox((0, 0), first_letter, font=font)
        text_width = textbbox[2] - textbbox[0]
        text_height = textbbox[3] - textbbox[1]

        vertical_offset = 90
        text_position = (
            (image_size[0] - text_width) / 2,
            (image_size[1] - text_height) / 2 - vertical_offset,
        )

        draw.text(text_position, first_letter, font=font, fill=self.text_color)

        image_path = f"profile_images/default/user_{instance.user.id}/default_profile_image_user_{instance.user.id}.png"
        full_path = os.path.join(settings.MEDIA_ROOT, image_path)

        user_folder = os.path.dirname(full_path)

        if not os.path.exists(user_folder):
            os.makedirs(user_folder, exist_ok=True)

        image.save(full_path)

        return image_path
