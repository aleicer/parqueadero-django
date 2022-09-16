from django.db import models

class Vehiculo(models.Model):
  placa = models.CharField(max_length=6)
  tipo_vehiculo = models.CharField(max_length=20)
