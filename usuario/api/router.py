from rest_framework.routers import DefaultRouter
from usuario.api.views import UsuarioApiViewSet

router_usuario = DefaultRouter()

router_usuario.register(prefix = 'usuario', basename = 'usuario', viewset = UsuarioApiViewSet)