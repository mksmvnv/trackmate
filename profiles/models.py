from django.db import models

from django.conf import settings


def avatar_upload_path(instance, filename):
    return f"profile_images/user_{instance.user.id}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(
        default="profile_images/default.jpg", upload_to=avatar_upload_path
    )
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    gender = models.CharField(max_length=128, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
