from django.db import models
from vehiculo.models import Vehiculo

class Ticket (models.Model):
    tarifa = models.IntegerField()
    hora_entrada = models.DateTimeField(blank=True, null=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    idVehiculo = models.ForeignKey(Vehiculo, null=True, on_delete= models.CASCADE)
    total_pagar = models.IntegerField()
    
    