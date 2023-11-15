from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from bookapp.models import Book
from bookshelfapp.models import Bookshelf


class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    review = models.TextField(null=True)
    transcription = models.TextField(null=True)
