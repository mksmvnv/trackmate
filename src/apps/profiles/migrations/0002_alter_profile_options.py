# Generated by Django 5.1.2 on 2024-10-17 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['id', 'user'], 'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
    ]
