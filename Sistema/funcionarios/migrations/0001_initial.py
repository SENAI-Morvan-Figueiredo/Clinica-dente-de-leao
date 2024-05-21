# Generated by Django 5.0.6 on 2024-05-21 07:20

import django.core.validators
import django.db.models.deletion
import django_cpf_cnpj.fields
import funcionarios.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=200, unique=True, verbose_name='Especialidades')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=200, verbose_name='Serviço')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descrição')),
                ('valor', models.FloatField(verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', django_cpf_cnpj.fields.CPFField(max_length=14)),
                ('genero', models.CharField(max_length=30, verbose_name='Genero')),
                ('telefone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="O número precisa estar neste formato:                         '+99 99 9999-0000'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('rua', models.CharField(max_length=200, verbose_name='Rua')),
                ('numero', models.CharField(max_length=15, verbose_name='Numero')),
                ('complemento', models.CharField(blank=True, max_length=200, verbose_name='Complemento')),
                ('municipio', models.CharField(max_length=20, verbose_name='Municipio')),
                ('unidade_federal', models.CharField(max_length=2, verbose_name='Unidade Federal')),
                ('data_nacimento', models.DateField(verbose_name='Data de Nacimento')),
                ('data_contratacao', models.DateField(verbose_name='Data de contratação')),
                ('is_medico', models.BooleanField(default=False, verbose_name='É medico')),
                ('is_ativo', models.BooleanField(default=True, verbose_name='Está ativo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('crm', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid_crm', message="O CRM precisa estar no seguinte formato:                                 'xxxxxxx-UF'", regex='^\\d{7}-\\d{2}$')], verbose_name='CRM')),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='especialidades', to='funcionarios.especialidade')),
                ('funcionario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='funcioanrios', to='funcionarios.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Ensira uma data', validators=[funcionarios.models.valida_dia])),
                ('horario', models.CharField(choices=[('1', '09:00'), ('2', '09:30'), ('3', '10:00'), ('4', '10:30'), ('5', '11:00'), ('6', '11:30'), ('7', '12:00'), ('8', '12:30'), ('9', '13:00'), ('10', '13:30'), ('11', '14:00'), ('12', '14:30'), ('13', '15:00'), ('14', '15:30'), ('15', '16:00'), ('16', '16:30'), ('17', '17:30'), ('18', '17:30'), ('19', '18:00')], max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Agenda', to='funcionarios.medico')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.servico')),
            ],
            options={
                'unique_together': {('horario', 'dia')},
            },
        ),
    ]
