from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Bienvenido a la página de inicio!")

def perfil(request):
    return HttpResponse("Esta es tu página de perfil.")
