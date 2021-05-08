from django.urls import path     
from . import views
urlpatterns = [
    path('friends', views.friends),
    path('add_friend/<int:id>', views.add_friend),
    path('remove_friend/<int:id>', views.remove_friend),
    path('view_profile/<int:id>', views.view_profile)
]