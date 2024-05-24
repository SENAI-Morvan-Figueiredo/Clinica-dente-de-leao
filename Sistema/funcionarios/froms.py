from django import forms
from . import models

class FuncionarioCreateForm(forms.Form):
    
    class Meta:
        model = models.Funcionario
        fields =  ['cpf', 'genero', 'telefone', 'cep', 'rua', 'numero', 'complemento', 'municipio', 'unidade_federal', 'data_nacimento', 'data_contratacao', 'is_medico'
    ]
        
class MedicoCreateForm(forms.Form):
    
    class Meta:
        model = models.Medico
        fields = ['nome', 'crm', 'funcionario', 'especialidade']