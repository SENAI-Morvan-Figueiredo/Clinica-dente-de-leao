# Generated by Django 5.0.6 on 2024-06-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_rename_name_funcionario_nome_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=models.DateTimeField(verbose_name='Horario'),
        ),
    ]
