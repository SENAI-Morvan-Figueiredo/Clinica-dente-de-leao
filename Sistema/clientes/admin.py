from django.contrib import admin
from .models import *

admin.site.register(Clientes)
admin.site.register(Convenio)
admin.site.register(PlanoConvenio)
admin.site.register(ServicoCoberto)
admin.site.register(ServicoPlano)