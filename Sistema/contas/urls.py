from django.contrib import admin
from django.urls import path
from .views import Login
urlpatterns = [
    path('entrar', Login.as_view(), name='login'),
]
