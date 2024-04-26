import holidays
from datetime import date
from django.db import models
from contas.models import User
from django_cpf_cnpj.fields import CPFField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import OneToOneField, ForeignKey

# Create your models here.

class Funcionario(models.Model):

    nome = models.CharField('Nome', max_length=200)
    cpf = CPFField(masked=True)
    
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=200)
    numero = models.CharField('Numero', max_length=20)
    municipio = models.CharField('Municipio', max_length=20)
    unidade_federal = models.CharField('Unidade Federal', max_length=2)
    complemento = models.CharField('Complemento', max_length=200, blank=True)
    
    data_nacimento = models.DateField('Data de Nacimento')
    data_contratacao = models.DateField('Data de contratação')
    is_medico = models.BooleanField('É medico', default=False)
    is_ativo = models.BooleanField('Está ativo', default=True)

    user_id = OneToOneField(User, on_delete=models.CASCADE, related_name='funcionarios')

    def __str__(self):
        return f'{self.nome}'
    

class Especialidade(models.Model):
    especialidade = models.CharField('Especialidades', max_length=200, unique=True)
    descricao = models.CharField('Descrição', max_length=1000)

    def __str__(self):
        return f'{self.especialidade}'

class Medico(models.Model):
    nome = models.CharField('Nome', max_length=200)
    crm = models.CharField('CRM', max_length=13,unique=True , validators=[
        RegexValidator(
            regex=r'^\d{7}-\d{2}$',
            message="O CRM precisa estar no seguinte formato: \
                                'xxxxxxx-UF'",
            code='Invalid_crm')
    ])
    funcionario = OneToOneField(Funcionario, on_delete=models.CASCADE, related_name='funcioanrios')
    especialidade = ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='especialidades' )

    def __str__(self):
        return f'{self.nome}'
    
def is_feriado(instance):
    lista_feriados = holidays.country_holidays('BR')

    if instance in lista_feriados[f'{date.year}-01-01' : f'{date.year}-12-31']:
        



def valida_dia(value):
    hoje = date.today()
    dia_semana = date.fromisoformat(f'{value}').weekday()

    if value < hoje:
        raise ValidationError('Não é possivel escolher uma data atrasada.')
    if dia_semana == 6:
        raise ValidationError('Escolha um dia util')

def gera_horarios(list, day):
    pass


class agenda(models.Model):
    
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='Agenda')
    dia = models.DateField(help_text='Ensira uma data', validators=[valida_dia])

    

    
    
     
