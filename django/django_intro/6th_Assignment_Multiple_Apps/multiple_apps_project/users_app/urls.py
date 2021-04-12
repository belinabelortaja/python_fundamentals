from django.urls import path    
from . import views
app_name = 'users_app'
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('users', views.users),
    path('users/new', views.register),
]