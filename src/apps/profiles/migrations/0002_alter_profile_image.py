# Generated by Django 5.1.5 on 2025-01-25 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.URLField(blank=True, default="", max_length=255, null=True),
        ),
    ]
