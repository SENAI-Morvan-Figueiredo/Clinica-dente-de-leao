from django.contrib import admin
from django.urls import path, include
from .views import ClienteCreateView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),
    path('clientes/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-delete')
    
]
