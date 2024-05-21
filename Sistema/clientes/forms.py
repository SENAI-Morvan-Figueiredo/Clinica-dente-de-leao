from django import forms
from . import models

class ClienteViewForm(forms.Form):
    model = models.Cliente
    fields=['cpf', 'genero', 'telefone', 'convenio', 'plano', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nacimento']