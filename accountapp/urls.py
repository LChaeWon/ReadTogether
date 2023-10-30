from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import main_page, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('main/', main_page, name='main'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
]