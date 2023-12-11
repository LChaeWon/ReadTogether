from django.db import models

from accountapp.models import User
from bookapp.models import Book


class Bookshelf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookshelf")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="bookshelf")






