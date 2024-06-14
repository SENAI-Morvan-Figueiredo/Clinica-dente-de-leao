from django.contrib import admin
from django.urls import path, include
# from django.urls.conf import include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),

    path('funcionarios/', include(('funcionarios.urls', 'funcionarios'),namespace='funcionarios')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace= 'clientes')),
    path('contas/', include(('accounts.urls', 'accounts'), namespace= 'accounts')),
]
