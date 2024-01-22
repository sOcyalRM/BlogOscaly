from django.urls import path
from . import views 

urlpatterns = [
    path('perfil/', views.profile, name='perfil'),
    path('perfil/<id>', views.publicacion, name='publicacion'),
]