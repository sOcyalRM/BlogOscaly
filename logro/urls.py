from django.urls import path
from . import views

urlpatterns = [
    path ('logro/', views.logro, name= 'logro'),
]