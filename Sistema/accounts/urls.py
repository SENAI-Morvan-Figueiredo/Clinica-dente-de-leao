from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('entrar/', views.login, name='login'),
    path('registrar/', views.singin, name='singin')
]
