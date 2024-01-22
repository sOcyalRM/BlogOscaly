from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('logro/', views.logro, name='logro'),
    path('contacto/', views.contacto, name='contacto'),
    path('tienda/', views.tienda, name='tienda'),
]