from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def tienda(request):
    return render(request, 'core/tienda.html')

