from django.urls import path     
from . import views
urlpatterns = [
    path('courses', views.index),
    path('courses/new', views.new),
    path('courses/create', views.create),
    path('courses/<int:id>', views.show),
    path('courses/<int:id>/destroy', views.destroy),
    path('courses/<int:id>/delete', views.delete),
    path('courses/<int:id>/comment', views.add_comment),
    path('courses/<int:id>', views.view_comment),

]