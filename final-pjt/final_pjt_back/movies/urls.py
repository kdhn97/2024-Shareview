from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_movie, name='download'),
    path('actors/', views.actor, name='actor'),
    path('delete/', views.delete, name='delete'),
]
