# Generated by Django 4.2.6 on 2023-12-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accountapp", "0002_remove_user_username_user_nickname"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile",
            field=models.ImageField(null=True, upload_to="profile/"),
        ),
    ]