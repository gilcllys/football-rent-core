from rest_framework import routers
from core import viewsets

router = routers.SimpleRouter()
router.register(r'usuarios', viewsets.UsuarioViewSet)
router.register(r'reservas', viewsets.ReservaViewSet)
router.register(r'football_field', viewsets.FootballFieldViewSet)
router.register(r'football_field_image', viewsets.FootballFieldImageViewSet)
router.register(r'payment', viewsets.PaymentViewSet)
urlpatterns = router.urls