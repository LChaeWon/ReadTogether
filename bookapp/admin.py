from django.contrib import admin

# Register your models here.
from bookapp.models import Book

admin.site.register(Book)