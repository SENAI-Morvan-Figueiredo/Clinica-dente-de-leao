from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.funcionario_cadastro, name='funcionario_cadastro')
]
