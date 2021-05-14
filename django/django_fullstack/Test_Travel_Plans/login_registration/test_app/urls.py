from django.urls import path     
from . import views
urlpatterns = [
    path('travels', views.travel_index),
    path('travels/create', views.create_travel),
    path('travels/new', views.new_travel),
    path('travels/<int:travel_id>/join_travel', views.join_travel),
    path('travels/destination/<int:travel_id>', views.show_travel)
]