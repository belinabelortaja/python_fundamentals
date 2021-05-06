from django.urls import path     
from . import views
urlpatterns = [
    path('books', views.books),
    path('books/create', views.create),
    path('books/show/<int:book_id>', views.show),
    path('books/<int:book_id>/add_favorite', views.add_favorite),
    path('books/<int:book_id>/unfavorite', views.un_favorite),
    path('books/<int:book_id>/update', views.update),
    path('books/delete/<int:book_id>', views.delete),
]