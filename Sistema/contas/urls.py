from django.contrib import admin
from django.urls import path
from .views import Login, RegisterView
urlpatterns = [
    path('entrar/', Login.as_view(), name='login'),
    path('registrar/', RegisterView.as_view(), name='singin')
]
