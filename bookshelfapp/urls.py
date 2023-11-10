
from django.urls import path

from bookshelfapp.views import BookShelfView, BookshelfListView

app_name = "bookshelfapp"

urlpatterns = [
    path('mybookshelf/',BookShelfView.as_view(), name='mybookshelf'),
    path('list/', BookshelfListView.as_view(), name='list'),

]