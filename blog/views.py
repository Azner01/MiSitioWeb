from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Inicio(request):
    return HttpResponse("¡Bienvenido a mi blog!")


