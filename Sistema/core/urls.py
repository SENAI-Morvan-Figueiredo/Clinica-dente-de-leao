from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('funcionarios/', include('funcionarios.urls', namespace= 'funcionarios')),
    path('clientes/', include('clientes.urls', namespace= 'clientes')),
    path('contas/', include('contas.urls', namespace= 'contas')),
]
