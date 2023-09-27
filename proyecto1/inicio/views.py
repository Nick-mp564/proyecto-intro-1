from django.shortcuts import render, redirect
from .forms import Crearuser
from .models import Publicacion, User

def news(request):
    return render(request, 'news.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html', 
        {'form': Crearuser})
    else:
        User.objects.create(email = request.POST['email'], psw = request.POST['psw']) 
        return redirect('/explore/')

def about(request):
    return render(request, 'about.html')

def explore(request): #con paisajes y recorridos
    return render(request, 'explore.html')

def inicio(request):
    Publicacion.objects.create(title = request.GET['title'], likes = request.GET['likes'], shared = request.GET['shared']) 
    return render(request, 'inicio.html', {'form': Publicacion})