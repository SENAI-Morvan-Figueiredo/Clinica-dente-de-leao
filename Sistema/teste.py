import holidays
from datetime import date
from django.core.exceptions import ValidationError


def valida_dia(value):
    hoje = date.today()
    dia_semana = date.fromisoformat(f'{value}').weekday()

    if value < hoje:
        raise ValidationError('Não é possivel escolher uma data atrasada.')
    
    if dia_semana == 6:
        raise ValidationError('Escolha um dia util')
    
    objeto_feriados = holidays.country_holidays('BR')
    ano = f'{date.today()}'

    for objeto_feriado in objeto_feriados[f'{ano[:5]}-01-01' : f'{ano[:5]}-12-31']:

        if value == objeto_feriado:
            raise ValidationError('')


def gera_horarios(dia):
    dia_semana = date.fromisoformat(f'{dia}').weekday()

    if :
        horarios = [(f'{i}', f'{i + 8}:{j}0' if i+8 > 9 else f'0{i + 8}:00') for i in range(1, 11) for j in range(0,4,3)]

        return horarios
    else:
        horarios = [(f'{i}', f'{i + 8}:00' if i+8 > 9 else f'0{i + 8}:00') for i in range(1, 5)]
        return horarios
    
teste = date.today()
print(teste)
lista_horarios = gera_horarios(teste)
print(lista_horarios)