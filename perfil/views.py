from django.shortcuts import render
from .models import Profile

# Create your views here.
def profile(request):
    profiles = Profile.objects.all()
    return render (request, 'perfil/perfil.html', {'profiles':profiles})

def publicacion(request, id):
    post = Profile.objects.get(id=id)
    return render (request, 'core/publicacion.html', {'post':post})