from django.db import models

from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
    bio = models.TextField()

    def __str__(self):
        return self.user.username
