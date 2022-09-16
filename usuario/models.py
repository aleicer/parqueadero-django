from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_documento = models.CharField(max_length=15)
    correo_electronico = models.CharField(max_length=50)
    clave = models.CharField(max_length=30)
 
