
from django.urls import path

from bookshelfapp.views import BookShelfView, BookshelfListView, ReviewWriteView, ReviewDetailView

app_name = "bookshelfapp"

urlpatterns = [
    path('mybookshelf/',BookShelfView.as_view(), name='mybookshelf'),
    path('list/', BookshelfListView.as_view(template_name='bookshelfapp/list.html'), name='list'),
    path('write/', ReviewWriteView.as_view(), name='write'),
    path('review/<int:pk>',ReviewDetailView.as_view(),name='review')

]