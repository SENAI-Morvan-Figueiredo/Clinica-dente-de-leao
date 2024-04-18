from django.db import models
from django.db.models.fields.related import ForeignKey
from contas.models import User


# Create your models here.

class Funcionario(models.Model):

    nome = models.CharField(verbose_name='Nome', max_length=200)
    user_id = ForeignKey(User.id)
    
