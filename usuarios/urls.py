from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, TrabajadorViewSet

router = DefaultRouter()
router.register(r'perfiles', UserProfileViewSet)
router.register(r'trabajadores', TrabajadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]