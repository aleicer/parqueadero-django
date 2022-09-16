from rest_framework.viewsets import ModelViewSet
from usuario.models import Usuario  
from usuario.api.serializer import UsuarioSerializer

class UsuarioApiViewSet(ModelViewSet):
  serializer_class = UsuarioSerializer
  queryset = Usuario.objects.all()