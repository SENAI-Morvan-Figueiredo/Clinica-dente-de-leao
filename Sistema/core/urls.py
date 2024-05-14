from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # path('funcionarios/', include('funcionarios.urls', namespace= 'funcionarios')),
    # path('clientes/', include('clientes.urls', namespace= 'clientes')),
    # path('contas/', include('contas.urls', namespace= 'contas')),
]
