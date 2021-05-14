from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('authors',views.authors),
    path('book/<id>',views.book),
    path('author/<id>',views.author2),
]