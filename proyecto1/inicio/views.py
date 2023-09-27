from django.shortcuts import render
from .forms import Crearuser

def noticias(request):
    return render(request, 'noticias.html')

def usuario(request):
    return render(request, 'Login.html', 
    {'form': Crearuser})

def sobre(request):
    return render(request, 'sobre.html')

def explorar(request): #con paisajes y recorridos
    return render(request, 'explorar.html')

def inicio(request):
    return render(request, 'inicio.html')