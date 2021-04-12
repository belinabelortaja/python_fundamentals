from django.urls import path    
from . import views
app_name = 'surveys_app'
urlpatterns = [
    path('', views.index),
    path('new', views.new),
]