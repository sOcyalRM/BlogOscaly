from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length = 200, verbose_name='Titulo')
    description = RichTextField(verbose_name = 'Descripcion')
    content = RichTextField (null = True, blank = True, verbose_name = 'Contenido')
    image = models.ImageField(upload_to="perfil", verbose_name= 'Imagen')
    link = models.URLField (null = True, blank = True, verbose_name = 'Enlace')
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now = True, verbose_name = 'Fecha de actualizacion')

    def __str__(self):
        return self.title   # Devuelve el titulo como nombre de post
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ["-created"]


