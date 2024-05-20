from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [        
    path('minha_conta/', views.index, name='index'),
    path('entrar/', views.login, name='login'),
    path('registrar/', views.singin, name='singup'),
    path('sair/', views.logout , name='logout')
    
]
