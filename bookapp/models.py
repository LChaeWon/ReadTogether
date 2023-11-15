

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book/')
    keyword = models.CharField(max_length=5)


