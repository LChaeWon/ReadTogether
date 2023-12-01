from django.urls import path

from reviewapp.views import ReviewWriteView, ReviewDeleteView, ReviewUpdateView, ReviewDetailView

app_name = "reviewapp"

urlpatterns = [
    path('write/', ReviewWriteView.as_view(), name='write'),
    path('delete/<int:pk>', ReviewDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', ReviewUpdateView.as_view(), name='update'),
    path('review/<int:pk>/<int:u_pk>', ReviewDetailView.as_view(), name='review')

]