from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [        
    path('minha-conta/', views.index, name='index'),
    path('entrar/', views.login, name='login'),
    path('registrar/', views.singin, name='singup'),
    path('', views.logout , name='logout'),
    
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
    
]
