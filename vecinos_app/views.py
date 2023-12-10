from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homeView(request):
    return HttpResponse("HOLAAAAA")

def inicio(request):
    return HttpResponse("¡Bienvenido a la página de inicio!")

def perfil(request):
    return HttpResponse("Esta es tu página de perfil.")