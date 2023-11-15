from django.urls import path

from reviewapp.views import ReviewWriteView

app_name = "reviewapp"

urlpatterns = [
    path('write/', ReviewWriteView.as_view(), name='write'),
]