# Generated by Django 4.2.6 on 2023-11-15 08:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookapp", "0005_remove_book_user"),
        ("bookshelfapp", "0012_alter_bookshelf_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="bookshelf",
            unique_together={("user", "book")},
        ),
    ]
