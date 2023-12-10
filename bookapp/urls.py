from django.urls import path

from bookapp.views import BookDetailView

app_name = "bookapp"

urlpatterns = [
    path('bookdetail/<int:pk>', BookDetailView.as_view(), name='detail'),
]