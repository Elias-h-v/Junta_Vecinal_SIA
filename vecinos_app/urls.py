from django.urls import path
from .views import info_socios, buscar_socio




urlpatterns =[
    #path('',homeView, name='home'),
    #path('perfil/', views.perfil),
    path('inicio/', info_socios, name='inicio'),
    path('buscar_socio/',buscar_socio, name='buscar_socio'),
    
]




