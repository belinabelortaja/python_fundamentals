from django.urls import path     
from . import views
urlpatterns = [
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:id>', views.show),
    path('shows', views.index),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/update', views.update),
    path('shows/<id>/delete',views.destroy),
]