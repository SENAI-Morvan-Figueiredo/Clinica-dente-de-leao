import holidays
from datetime import date


def is_feriado(value):
    objeto_feriados = holidays.country_holidays('BR')
    ano = f'{date.today()}'
    lista_feriados = []
    for objeto_feriado in objeto_feriados[f'{ano[:5]}-01-01' : f'{ano}-12-31']:
        lista_feriados.append(objeto_feriado)   

    if value in lista_feriados:
        return True
    else:
        return False
    
def gera_horarios(dia):
    horarios = []
    
    if not is_feriado(dia):
        horarios = [(f'{i}', f'{(i + 8) + ':00'}' if len(i+8) < 2 else f'{'0'+(i + 8) + ':00'}') for i in range(1, 10)]
        return horarios
    else:
        horarios = [(f'{i}', f'{(i + 8) + ':00'}' if len(i+8) < 2 else f'{'0'+(i + 8) + ':00'}') for i in range(1, 4)]

teste = date.today()
print(teste)
lista_horarios = gera_horarios(teste)

