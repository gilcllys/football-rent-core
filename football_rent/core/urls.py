from rest_framework import routers
from core import viewsets

router = routers.SimpleRouter()
router.register(r'usuarios', viewsets.UsuarioViewSet)
urlpatterns = router.urls