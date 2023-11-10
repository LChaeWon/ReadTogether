# Generated by Django 4.2.6 on 2023-11-08 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0002_remove_book_booknumber_alter_book_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bookshelfapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookshelf",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mybookshelf",
                to="bookapp.book",
            ),
        ),
        migrations.AlterField(
            model_name="bookshelf",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mybookshelf",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
