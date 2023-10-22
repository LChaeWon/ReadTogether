from django.urls import path

from accountapp.views import main_page

app_name = "accountapp"

urlpatterns = [
    path('main/', main_page, name='main')
]