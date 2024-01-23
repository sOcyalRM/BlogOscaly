from django.shortcuts import render
from .forms import Contact

# Create your views here.
def contact(request):
    contact_form = Contact()

    if request.method == "POST":
        contact_form = Contact(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            mail = request.POST.get('mail','')
            content = request.POST.get('content','')

    return render(request, 'contact/contacto.html', {'form':contact_form})

#Continuar desde aqui...