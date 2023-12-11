from django.shortcuts import render
from .models import Socios
# Create your views here.
from django.http import HttpResponse

def homeView(request):
    return HttpResponse("HOLAAAAA")

#def inicio(request):
#    return HttpResponse("¡Bienvenido a la página de inicio!")

def perfil(request):
    return HttpResponse("Esta es tu página de perfil.")

def info_socios(request):
   socios_lista = Socios.objects.all()
   return render(request,"info_socio.html",{"Socios":socios_lista})