from django.db import models
from django.conf import settings
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.db.models.fields.related import ManyToManyField, OneToOneField, ForeignKey


class Convenio(models.Model):
    convenio = models.CharField('Convenio', max_length=200)
    cnpj = CNPJField(masked=True)

class ServicoCoberto(models.Model):
    servico = models.CharField('Serviços', max_length=200)
    descricao = models.CharField('Descrição', max_length=1000)

class PlanoConvenio(models.Model):
    plano = models.CharField('Plano', max_length=30)
    convenio = ForeignKey(Convenio, on_delete=models.CASCADE, related_name='plano_convenio')

class ServicoPlano(models.Model):
    servico = ManyToManyField(ServicoCoberto, related_name='serviço_plano')
    plano = ManyToManyField(PlanoConvenio, related_name='servico_plano')

class Clientes(models.Model):

    nome = models.CharField('Nome', max_length=200)
    cpf = CPFField(masked=True)
    
    GENERO = (
        ("MAS", "Masculino"),
        ("FEM", "Feminino"),
        ("OTR", "Outro"),
    )
    
    genero = models.CharField(max_length=9, choices=GENERO)
    
    convenio = ForeignKey(Convenio, on_delete=models.CASCADE, related_name='clientes')
    plano = ForeignKey(PlanoConvenio, on_delete=models.CASCADE, related_name='clientes')
    
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=200)
    numero = models.CharField('Numero', max_length=15)
    complemento = models.CharField('Complemento', max_length=200, blank=True, null=True)
    municipio = models.CharField('Municipio', max_length=20)
    unidade_federal = models.CharField('Unidade Federal', max_length=2)
    
    data_nacimento = models.DateField('Data de Nacimento')
    data_inicio = models.DateField('Data de Inicio')
    
    is_ativo = models.BooleanField('Está ativo', default=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.nome}'