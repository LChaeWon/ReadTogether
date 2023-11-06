from django.contrib.auth.models import User
from django.db import models

from bookapp.models import Book


class Bookshelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mybookshelf')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='mybookshelf')

    class Meta:
        unique_together = ('user','book')
