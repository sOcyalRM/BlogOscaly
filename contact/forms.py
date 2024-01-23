from django import forms

class Contact(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs = {'class':'cont_nombrecompleto',  'id':'l_nombre',  'placeholder':"Ej.:Juan Ramirez"}
    ))  # required = True para que sea mandatorio llenar el campo
    mail = forms.EmailField(label= "Email", required=True, widget=forms.EmailInput(
        attrs={'class':'cont_email', 'id':'c_electronico', 'placeholder':'Ej.:jramirez@example.com'}
    ))
    content = forms.CharField(label = "Mensaje", required=True, widget=forms.Textarea(
        attrs={ 'placeholder':'Maximo 300 caracteres...', 'id':'l_texto', 'maxlength':'300'}
    ))
