from django.contrib import admin

from usuario.models import Usuario

@admin.register(Usuario)
class UsusarioAdmin(admin.ModelAdmin):
  list_display = ['id', 'nombre','apellido']
