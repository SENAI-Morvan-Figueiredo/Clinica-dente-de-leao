# Generated by Django 5.0.6 on 2024-05-09 01:00

import django.db.models.deletion
import django.utils.timezone
import funcionarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.CharField(max_length=200, verbose_name='Serviço')),
                ('descricao', models.CharField(max_length=1000, verbose_name='Descrição')),
                ('valor', models.FloatField(verbose_name='Valor')),
            ],
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='especialidade_Id',
            new_name='especialidade',
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='funcionario_id',
            new_name='funcionario',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='genero',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, verbose_name='Genro'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='numero',
            field=models.CharField(max_length=15, verbose_name='Numero'),
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Ensira uma data', validators=[funcionarios.models.valida_dia])),
                ('horario', models.CharField(choices=[('1', '09:00'), ('2', '10:00'), ('3', '11:00'), ('4', '12:00'), ('5', '13:00'), ('6', '14:00'), ('7', '15:00'), ('8', '16:00'), ('9', '17:00'), ('10', '18:00')], max_length=30, verbose_name='Horario')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Agenda', to='funcionarios.medico')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.servico')),
            ],
        ),
    ]