from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.db.models.fields.related import ManyToManyField, OneToOneField, ForeignKey
from funcionarios.models import *
from accounts.models import *

class Convenio(models.Model):
    convenio = models.CharField('Convenio', max_length=200)
    cnpj = CNPJField(masked=True)
    
    def __str__(self):
        return f'{self.convenio}'

class ServicoCoberto(models.Model):
    servico = models.CharField('Serviços', max_length=200)
    descricao = models.CharField('Descrição', max_length=1000)
    
    def __str__(self):
        return f'{self.servico}'

class PlanoConvenio(models.Model):
    plano = models.CharField('Plano', max_length=30)
    convenio = ForeignKey(Convenio, on_delete=models.CASCADE, related_name='plano_convenio')
    
    def __str__(self):
        return f'{self.plano}-{self.convenio}'

class ServicoPlano(models.Model):
    servico = ManyToManyField(ServicoCoberto, related_name='serviço_plano')
    plano = ManyToManyField(PlanoConvenio, related_name='servico_plano')
    
    def __str__(self):
        return f'{self.servico}-{self.plano}'

class Cliente(models.Model):
    
    nome = models.CharField(verbose_name='Nome', max_length=30)
    sobrenome = models.CharField(verbose_name='Sobremone', max_length=200)

    cpf = CPFField(verbose_name="CPF", max_length=50, unique=True,)
    
    GENERO = (
        ("MAS", "Masculino"),
        ("FEM", "Feminino"),
        ("OTR", "Outro"),
    )
    
    genero = models.CharField(verbose_name="Genero", max_length=9, choices=GENERO)
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="O número precisa estar neste formato: \
                        '+99 99 9999-0000'."
    )
    telefone = models.CharField(verbose_name="Telefone", validators=[phone_regex],max_length=17, null=True, blank=True)
    
    
    convenio = ForeignKey(Convenio, on_delete=models.CASCADE, related_name='clientes')
    plano = ForeignKey(PlanoConvenio, on_delete=models.CASCADE, related_name='clientes')
    
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=200)
    numero = models.CharField('Numero', max_length=15)
    complemento = models.CharField('Complemento', max_length=200, blank=True, null=True)
    municipio = models.CharField('Municipio', max_length=20)
    unidade_federal = models.CharField('Unidade Federal', max_length=2)
    
    data_nacimento = models.DateField('Data de Nacimento')
    data_inicio = models.DateField('Data de Inicio', auto_now_add=True)
    
    is_ativo = models.BooleanField('Está ativo', default=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.nome}'
    
class Consulta(models.Model):
    agenda =  OneToOneField(Agenda, on_delete=models.CASCADE, related_name='consulta')
    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='consulta')
    
    class Meta:
        unique_together = ('agenda', 'cliente')
        
    def __str__(self):
        return f'{self.agenda} - {self.cliente}'