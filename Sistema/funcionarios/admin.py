from django.contrib import admin
from .models import Funcionario, Especialidade, Medico

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Especialidade)
admin.site.register(Medico)
