
from django.urls import path

from bookshelfapp.views import BookShelfView

app_name = "bookshelfapp"

urlpatterns = [
    path('mybookshelf/',BookShelfView.as_view(), name='mybookshelf')
]