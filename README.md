# 🦁 Sistema POS - Parque Safari (Backend)

Backend oficial para el sistema de Punto de Venta (POS) *On-Premise* del **Parque Safari**, desarrollado bajo una arquitectura robusta en capas, orientado a la gestión de salón, mesas, catálogo de productos, control de trabajadores (consumo interno/fiado) y emisión de comandas sectorizadas.

---

## 🚀 Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Framework Web:** Django (con filosofía *Batteries-Included*)
* **API REST:** Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL
* **Seguridad:** Autenticación por roles (Administrador, Cajero, Garzón) y protección nativa contra SQL Injection y CSRF.

---

## 📂 Estructura del Proyecto
El proyecto está modularizado en aplicaciones independientes de Django para garantizar escalabilidad y mantenimiento:
* `usuarios/`: Gestión de perfiles de usuario, roles y trabajadores con control de fiado.
* `mesas/`: Control del salón y mapa de mesas (numeración alfanumérica de la A1 a la H7).
* `productos/`: Catálogo de menú (comidas, bebidas, snacks) y asignación de impresoras de destino (Cocina/Barra).
* `ventas/`: Manejo de jornadas de venta, transacciones, detalles y generación automática de comandas.

---

## ⚙️ Configuración y Despliegue Local

Sigue estos pasos para levantar el entorno de desarrollo en tu computador:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/parquesafari-pos-backend.git](https://github.com/TU_USUARIO/parquesafari-pos-backend.git)
cd parquesafari-pos-backend

2. Crear y activar el entorno virtual
Bash
python -m venv venv
# En Windows (CMD / PowerShell):
venv\Scripts\activate
3. Instalar dependencias
Bash
pip install django djangorestframework psycopg2-binary django-cors-headers
4. Configurar la Base de Datos en PostgreSQL
Asegúrate de tener PostgreSQL corriendo y crea una base de datos llamada parque_safari_db. Luego, en parquesafari_pos/settings.py, configura tus credenciales:

Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'parque_safari_db',
        'USER': 'tu_usuario_postgres',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Aplicar Migraciones
Bash
python manage.py makemigrations
python manage.py migrate
6. Crear un Superusuario (Opcional para el Admin de Django)
Bash
python manage.py createsuperuser
7. Ejecutar el Servidor
Bash
python manage.py runserver
El backend estará disponible en http://127.0.0.1:8000/.

🔌 Endpoints Principales de la API REST
Puedes explorar la API interactiva en formato navegable mediante los siguientes endpoints:

Administración Django: /admin/

Usuarios y Trabajadores: /api/usuarios/perfiles/ | /api/usuarios/trabajadores/

Mesas (Salón A1-H7): /api/mesas/mesas/

Catálogo de Productos: /api/productos/productos/

Ventas y Comandas: /api/ventas/ventas/ | /api/ventas/comandas/

Desarrollado para la asignatura de Ingeniería de Software / Proyecto Integrado - INACAP Rancagua.
