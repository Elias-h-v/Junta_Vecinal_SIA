from django.urls import path
from .views import info_socios
from . import views

urlpatterns =[
    #path('',homeView, name='home'),
    #path('perfil/', views.perfil),
    path('inicio/', views.info_socios),
]
