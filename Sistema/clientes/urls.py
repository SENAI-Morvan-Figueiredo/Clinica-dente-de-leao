from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registrar/dados-complementares/', views.cliente_cadastro, name='cliente_cadastro'),
    path('atualizar/', views.cliente_atualizar, name='cliente_atualizar'),
    
    path('cadatro/convenio/', views.cliente_atualizar, name='convenio_cadatro'),
    path('cadatro/convenio/plano', views.cliente_atualizar, name='convenio_cadatro'),
    
    # path('consultas/', views.consulta_lista, name='consulta_list'),
    # path('consultas/criar/', views.consulta_cadastro, name='consulta_create'),
    # path('consultas/editar/<int:pk>/', views.consulta_atualizar, name='consulta_update'),
    # path('consultas/excluir/<int:pk>/', views.consulta_excluir, name='consulta_delete'),
]
