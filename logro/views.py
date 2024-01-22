from django.shortcuts import render
from .models import Achievements

# Create your views here.
def logro(request):
    logros = Achievements.objects.all()
    return render (request, 'logro/logro.html', {'logros':logros})
