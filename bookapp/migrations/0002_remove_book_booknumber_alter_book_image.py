# Generated by Django 4.2.6 on 2023-11-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="booknumber",
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(upload_to="book/"),
        ),
    ]