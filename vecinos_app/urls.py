from django.urls import path
from .views import homeView, info_socios, perfil
from . import views

urlpatterns =[
    path('',homeView, name='home'),
    path('inicio/', views.info_socios),
    path('perfil/', views.perfil),
]
