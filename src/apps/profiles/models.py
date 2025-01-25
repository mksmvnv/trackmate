import os
import uuid

from django.db import models
from django.conf import settings

from django_enumfield import enum


class Gender(enum.Enum):
    Default = 0
    Male = 1
    Female = 2
    Other = 3

    __labels__ = {
        0: "Не указан",
        1: "Мужской",
        2: "Женский",
        3: "Другое",
    }


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE
    )
    image = models.URLField(max_length=255, blank=True, null=True, default="")
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    profession = models.CharField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = enum.EnumField(enum=Gender, default=Gender.Default)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "profiles"
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        ordering = ["id", "user"]

    def __str__(self):
        return self.user.username
