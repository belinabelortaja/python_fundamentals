from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.registration),
    path('wall', views.wall),
    path('login', views.login),
    path('logout', views.logout),
    path('post-message', views.post_message),
    path('post-comment/<int:id>', views.post_comment),
    path('delete/<int:id>', views.destroy),
]