from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.result),
    path('go_back', views.go_back),
]