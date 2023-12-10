from django.urls import path
from .views import homeView
from . import views

urlpatterns =[
    path('',homeView, name='home'),
    path('', views.inicio, name='mi_vista_principal'),
    path('perfil/', views.perfil, name='perfil'),
]
