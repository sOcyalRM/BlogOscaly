from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
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

            #Creamos correo 
            mail = EmailMessage (
                "Blog de Oscaly: Nuevo mensaje de contacto", #Asunto
                "De {} {}\n\nEscribio:\n\n{}".format(name,mail,content), #message
                "blogoscaly.com", #email de origen
                ["oscalyrmateo@gmail.com"], #Email de destino
                reply_to=[mail]
            )

            #Envio email y redirecciono
            try:
                mail.send()
                return redirect(reverse('contact')+"?exitoso")
            except:
                return redirect(reverse('contact')+"?fail")
                
    return render(request, 'contact/contacto.html', {'form':contact_form})

