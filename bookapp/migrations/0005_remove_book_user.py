# Generated by Django 4.2.6 on 2023-11-10 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0004_rename_like_users_book_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="user",
        ),
    ]
