from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('about/', views.about),
    path('news/', views.news),
    path('explore/', views.explore),
    path('inicio/', views.inicio)
]