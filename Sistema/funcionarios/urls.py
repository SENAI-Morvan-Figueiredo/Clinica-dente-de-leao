from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.funcionario_cadastro, name='funcionario_cadastro'),
    path('lista/', views.funionarios_lista, name='funcionario_lista'),
    
    path('agendas/', views.agenda_lista, name="agenda_lista"),
    path('agendar/', views.agenda_cadastro, name='agenda_cadastro'),
    path('agendar/atualizar/<int:pk>/', views.agenda_atualizar, name='agendar_consulta_atualizar'),
    path('agendar/apagar/<int:pk>/', views.agenda_deletar, name='agendar_consulta_deletar'),
    
    path('medico/lista/', views.medico_lista, name="medico_lista"),
    path('funcionarios/medico/cadastro', views.medico_cadastro, name='medico_cadastro'),
    path('medico/especialidade/cadastro/', views.especialidade_cadastro, name='especialidade_cadastro'),
    path('medico/especialidade/lista/', views.especialidade_lista, name="especialidade_lista"),
]
