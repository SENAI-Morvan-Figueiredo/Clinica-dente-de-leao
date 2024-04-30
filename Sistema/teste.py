import holidays
from datetime import date


def is_feriado(dia):
    objeto_feriados = holidays.country_holidays('BR')
    ano = f'{date.today()}'
    # lista_feriados = []
    for objeto_feriado in objeto_feriados[f'{ano[:5]}-01-01' : f'{ano[:5]}-12-31']:

        if dia == objeto_feriado:
            return True
        else:
            pass
    
def gera_horarios(dia):
    horarios = []
    
    if not is_feriado(dia):
        horarios = [(f'{i}', f'{i + 8}:{j}0' if i+8 > 9 else f'0{i + 8}:00') for i in range(1, 11) for j in range(0,4,3)]
        return horarios
    else:
        horarios = [(f'{i}', f'{i + 8}:00' if i+8 > 9 else f'0{i + 8}:00') for i in range(1, 5)]
        return horarios
    
teste = date.today()
print(teste)
lista_horarios = gera_horarios(teste)
print(lista_horarios)

