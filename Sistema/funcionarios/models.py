import holidays
from datetime import date
from django.db import models
from contas.models import User
from django_cpf_cnpj.fields import CPFField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import OneToOneField, ForeignKey

class Funcionario(models.Model):

    nome = models.CharField('Nome', max_length=200)
    cpf = CPFField(masked=True)
    genero = models.CharField('Genero', max_length=30)
    
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=200)
    numero = models.CharField('Numero', max_length=15)
    complemento = models.CharField('Complemento', max_length=200, blank=True)
    municipio = models.CharField('Municipio', max_length=20)
    unidade_federal = models.CharField('Unidade Federal', max_length=2)
    
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
    
def is_feriado(dia):
    objeto_feriados = holidays.country_holidays('BR')
    ano = f'{date.today()}'

    for objeto_feriado in objeto_feriados[f'{ano[:5]}-01-01' : f'{ano[:5]}-12-31']:

        if dia == objeto_feriado:
            return True

def valida_dia(value):
    hoje = date.today()
    dia_semana = date.fromisoformat(f'{value}').weekday()

    if value < hoje:
        raise ValidationError('Não é possivel escolher uma data atrasada.')
    
    elif is_feriado(value) or dia_semana == 6:
        raise ValidationError('Escolha um dia util')

# to do: gerador de horarios

# def gera_horarios(dia):
#     horarios = []
    
#     if not is_feriado(dia):
#         horarios = [(f'{i}', f'{i + 8}:{j}0' if i+8 > 9 else f'0{i + 8}:00') for i in range(1, 11) for j in range(0,4,3)]
        
#         return horarios
#     else:
#         horarios = [(f'{i}', f'{i + 8}:00' if i+8 > 9 else f'0{i + 8}:00') for i in range(1, 5)]
#         return horarios


class Servico(models.Model):
    servico = models.CharField('Serviço', max_length=200)
    descricao = models.CharField('Descrição', max_length=1000)
    valor = models.FloatField('Valor')




class Agenda(models.Model):
    
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='Agenda')
    dia = models.DateField(help_text='Ensira uma data', validators=[valida_dia])

    HORARIOS = (
        ('1', '09:00'),
        ('2', '10:00'),
        ('3', '11:00'),
        ('4', '12:00'),
        ('5', '13:00'),
        ('6', '14:00'),
        ('7', '15:00'),
        ('8', '16:00'),
        ('9', '17:00'),
        ('10', '18:00'),
    )

    horario = models.CharField('Horario',max_length=30, choices=HORARIOS)
    servico = ForeignKey(Servico, on_delete=models.CASCADE)