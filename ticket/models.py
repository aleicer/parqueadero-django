from django.db import models
from vehiculo.models import Vehiculo

class Ticket (models.Model):
    tarifa = models.IntegerField()
    hora_entrada = models.DateTimeField(auto_now_add = True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    idVehiculo = models.ForeignKey(Vehiculo, null=True, on_delete= models.CASCADE)
    
    