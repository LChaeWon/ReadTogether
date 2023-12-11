
from django.urls import path

from bookshelfapp.views import BookShelfView, BookshelfListView

app_name = "bookshelfapp"

urlpatterns = [
    path('mybookshelf/',BookShelfView.as_view(), name='mybookshelf'),
    path('list/<int:pk>', BookshelfListView.as_view(template_name='bookshelfapp/list.html'), name='list'),

]