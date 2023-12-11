from django.db import models

# Create your models here.
from accountapp.models import User
from bookapp.models import Book
from bookshelfapp.models import Bookshelf


class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE, related_name="review")
    review = models.TextField(null=True)
    transcription = models.TextField(null=True)
