
from django.db import models


KEYWORD_CHOICES=[
    ('novel','소설'),
    ('human','인문'),
    ('self','자기계발'),
    ('science','과학')
]
class Book(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book/')
    keyword = models.CharField(max_length=10,choices=KEYWORD_CHOICES)


