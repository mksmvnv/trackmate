# Generated by Django 5.1 on 2024-09-09 16:53

import django.db.models.deletion

from django.db import migrations, models
from django.conf import settings

import apps.profiles.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=apps.profiles.utils.FilePathProcessor(
                            "profile_images/"
                        ),
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=128, null=True)),
                ("last_name", models.CharField(blank=True, max_length=128, null=True)),
                ("profession", models.CharField(blank=True, max_length=128, null=True)),
                ("location", models.CharField(blank=True, max_length=128, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("М", "Мужской"), ("Ж", "Женский"), ("Д", "Другое")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("age", models.IntegerField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "profile",
                "verbose_name_plural": "profiles",
                "db_table": "profiles",
            },
        ),
    ]
