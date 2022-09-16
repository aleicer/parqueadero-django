from django.contrib import admin

from vehiculo.models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
  list_display = ['id', 'placa','tipo_vehiculo']
