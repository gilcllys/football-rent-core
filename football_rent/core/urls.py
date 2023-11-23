from rest_framework import routers
from core import viewsets

router = routers.SimpleRouter()
router.register(r'usuarios', viewsets.UsuarioViewSet)
router.register(r'reservas', viewsets.ReservaViewSet)
urlpatterns = router.urls