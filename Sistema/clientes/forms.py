from django import forms
from . import models

class ClienteForm(forms.Form):
    class Meta:
        model = models.Cliente
        fields = ['cpf', 'genero', 'telefone', 'convenio', 'plano', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nacimento']
        # fields = '__all__'
class ConvenioForm(forms.Form):
    class Meta:
        model = models.Convenio
        fields = ['convenio', 'cnpj']

class PlanoForm(forms.Form):
    class Meta:
        model = models.Convenio
        fields = ['plano', 'convenio']