# Generated by Django 4.2.6 on 2023-11-15 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0005_remove_book_user"),
        ("reviewapp", "0002_alter_review_book"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="user",
            new_name="writer",
        ),
        migrations.AlterField(
            model_name="review",
            name="book",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review",
                to="bookapp.book",
            ),
        ),
    ]