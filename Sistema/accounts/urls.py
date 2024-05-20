from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import  LogoutView

urlpatterns = [
    path('entrar/', views.login, name='login'),
    path('registrar/', views.singin, name='singin'),
    path('sair/', views.logout , name='logout')
]
