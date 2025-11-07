import re
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(
        verbose_name='Usuario', max_length=30, unique=True, validators=[
            RegexValidator(
                regex= re.compile('^[\w.@+-]+$'),
                message='Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os carecteres: @/./+/-/_.',
                code= 'invalid'
                )
        ], help_text= 'Um nome curto que será usado'+
                    ' para identificá-lo de forma única na plataforma.'
    )

    name = models.CharField(verbose_name='Nome', max_length=30)
    last_name = models.CharField(verbose_name='Sobremone', max_length=200)
    email = models.EmailField(verbose_name='Email', unique=True)
    is_staff = models.BooleanField(verbose_name='is_staff', default=False)
    is_active = models.BooleanField(verbose_name='Está Ativo', default=True)
    date_joined = models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    
    

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username
    
    def get_full_name(self):
        return f'{self.name} {self.last_name}'


