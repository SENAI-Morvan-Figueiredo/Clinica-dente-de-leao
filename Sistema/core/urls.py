from django.contrib import admin
from django.urls import path, include
# from django.urls.conf import include
from .views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    # path('funcionarios/', include('funcionarios.urls', namespace= 'funcionarios')),
    # path('clientes/', include(('clientes.urls', 'clientes'), namespace= 'clientes')),
    path('contas/', include(('contas.urls', 'contas'), namespace= 'contas')),
]
