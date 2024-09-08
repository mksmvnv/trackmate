import os

from django.contrib.staticfiles import finders
from django.utils.deconstruct import deconstructible

from PIL import Image, ImageDraw, ImageFont


@deconstructible
class FilePathProcessor:
    def __init__(self, path: str) -> None:
        self.path = path

    def __call__(self, instance: object, filename: str) -> str:
        ext = filename.split(".")[-1]
        filename = f"profile_image_user_{instance.user.id}.{ext}"
        user_folder = os.path.join(self.path, f"user_{instance.user.id}")
        full_path = os.path.join(user_folder, filename)

        default_image_path = (
            f"profile_images/default_profile_image_user_{instance.user.id}.png"
        )

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        if os.path.exists(full_path) and full_path != os.path.join(
            "media", default_image_path
        ):
            os.remove(full_path)

        return full_path


class FilePathManager:
    def __init__(self, base_path: str):
        self.processor = FilePathProcessor(base_path)

    def get_upload_path(self, instance: object, filename: str) -> str:
        return self.processor(instance, filename)


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

    def generate_image(self, instance):
        first_letter = instance.user.username[0].upper()
        img_size = (500, 500)
        img = Image.new("RGB", img_size, color=self.background_color)
        draw = ImageDraw.Draw(img)

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
            (img_size[0] - text_width) / 2,
            (img_size[1] - text_height) / 2 - vertical_offset,
        )

        draw.text(text_position, first_letter, font=font, fill=self.text_color)

        image_path = f"profile_images/default_profile_image_user_{instance.user.id}.png"
        full_path = os.path.join("media", image_path)

        user_folder = os.path.dirname(full_path)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        img.save(full_path)

        return image_path
