from django.db import models
from django.db.models.fields.related import ForeignKey
from contas.models import User
from django_cpf_cnpj.fields import CPFField

# Create your models here.

class Funcionario(models.Model):

    nome = models.CharField('Nome', max_length=200)
    cpf = CPFField('CPF', max_length=50, unique=True)
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=200)
    numero = models.CharField('Numero', max_length=20)
    complemento = models.CharField('Complemento', max_length=200, blank=True)
    data_nacimento = models.DateField('Data de Nacimento')
    data_contratacao = models.DateField('Data de contratação')
    is_medico = models.BooleanField('É medico', default=False)
    user_id = ForeignKey(User, on_delete=models.CASCADE, related_name='funcionarios', unique=True)
    
