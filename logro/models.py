from django.db import models

# Create your models here.
class Achievements(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    content = models.TextField(verbose_name = 'Contenido')
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