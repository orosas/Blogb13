from django.conf.urls import url, include
from django.contrib import admin

# para cargar media y static
from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^users/', include('modules.Usuarios.urls_api')),
    #TODO agregar publicaciones
]