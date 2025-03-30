from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('signup/', views.Signup_View.as_view(), name='signup'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
]