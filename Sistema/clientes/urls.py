from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('registrar/dados-complementares/', views.cliente_cadastro, name='cliente_cadastro'),
    path('atualizar/', views.cliente_atualizar, name='cliente_atualizar'),
    path('lista/clientes', views.cliente_lista, name='cliente_lista'),
    
    
    path('cadatro/convenio/', views.cliente_atualizar, name='convenio_cadatro'),
    path('cadatro/convenio/plano', views.cliente_atualizar, name='convenio_cadatro'),
    path('lista/convenio', views.convenio_lista, name='convenio_lista'),
    path('lista/convenio/plano', views.plano_lista, name='plano_lista'),
    
    
    path('consultas/criar/', views.consulta_cadastro, name='consulta_cadastro'),
    path('consultas/', views.consulta_lista, name='consulta_lista'),
    
    path('consultas/editar/<int:pk>/', views.consulta_atualizar, name='consulta_update'),
    path('consultas/excluir/<int:pk>/', views.consulta_excluir, name='consulta_delete'),
]
