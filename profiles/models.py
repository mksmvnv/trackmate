import os

from django.db import models
from django.conf import settings

from profiles.utils import FilePathManager, ImageGenerator


class Profile(models.Model):
    GENDER_CHOICES = [
        ("М", "Мужской"),
        ("Ж", "Женский"),
        ("Д", "Другое"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=FilePathManager("profile_images/").get_upload_path,
        blank=True,
        null=True,
    )
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    profession = models.CharField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "profiles"
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        default_image_path = (
            f"profile_images/default_profile_image_user_{self.user.id}.png"
        )

        if not self.image or self.image.name == default_image_path:
            self.image = ImageGenerator().generate_image(self)

        super().save(*args, **kwargs)


class ProfileImageManager:
    def __init__(self, instance):
        self.instance = instance
        self.default_image_path = (
            f"profile_images/default_profile_image_user_{self.instance.user.id}.png"
        )

    def get_old_image(self) -> str:
        try:
            return Profile.objects.get(pk=self.instance.pk).image
        except Profile.DoesNotExist:
            return None

    def is_default_image(self, image_path) -> bool:
        return image_path == os.path.join(settings.MEDIA_ROOT, self.default_image_path)

    def remove_old_image(self) -> None:
        old_image = self.get_old_image()
        new_image = self.instance.image

        if old_image and old_image != new_image:
            old_image_path = old_image.path

            if not self.is_default_image(old_image_path):
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)

    def set_default_image_if_needed(self) -> None:
        if not self.instance.image:
            self.instance.image = self.default_image_path
