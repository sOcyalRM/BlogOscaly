from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Achievements(models.Model):
    #Crear nuevo id aqqui : ID = models.IDField(null = True, blank = True)
    title = models.CharField(max_length = 200, verbose_name = 'Titulo')
    description = RichTextField(verbose_name = 'Descripcion')
    content = RichTextField(verbose_name = 'Contenido')
    image = models.ImageField(verbose_name= 'Imagen', upload_to= 'logro')
    link = models.URLField(null = True, blank = True, verbose_name = 'Enlace')
    created = models.DateTimeField(verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(verbose_name = 'Fecha de actualizacion')

    def __str__(self):
        return self.title   # Devuelve el titulo como nombre de post
    
    class Meta:
        verbose_name = 'Logro'
        verbose_name_plural = 'Logros'
        ordering = ["-created"]