from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.usuario),
    path('sobre/', views.sobre),
    path('noticias/', views.noticias),
    path('explorar/', views.explorar),
    path('', views.inicio)
]