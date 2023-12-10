from django.urls import path

from bookapp.views import BookDetailView, search

app_name = "bookapp"

urlpatterns = [
    path('bookdetail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('search/', search, name='search'),

]