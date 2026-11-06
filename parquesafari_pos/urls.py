from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/mesas/', include('mesas.urls')),
    path('api/productos/', include('productos.urls')),
    path('api/ventas/', include('ventas.urls')),
]