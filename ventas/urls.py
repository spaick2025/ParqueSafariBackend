from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JornadaVentaViewSet, VentaViewSet, DetalleVentaViewSet, ComandaViewSet

router = DefaultRouter()
router.register(r'jornadas', JornadaVentaViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalles-venta', DetalleVentaViewSet)
router.register(r'comandas', ComandaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]