from distutils.command.upload import upload
from djmoney.models.fields import MoneyField
from tinymce import models as tinymce_models
from django.db import models


class Producto (models.Model):
    nombre = models.CharField ( max_length = 60)
    precio = MoneyField ( default = 0, default_currency = 'MXN', max_digits = 11)
    descripcion = tinymce_models.HTMLField ()
    imagen = models.ImageField ( upload_to = "productos", null = True)
    agregado = models.DateTimeField (auto_now_add = True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = [ 'agregado']