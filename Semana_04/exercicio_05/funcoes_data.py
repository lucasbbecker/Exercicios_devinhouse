from datetime import datetime, date

def dia_da_semana(data_str):
    """Recebe uma data (formato DD/MM/AAAA) e retorna o dia da semana"""
    data = datetime.strptime(data_str, "%d/%m/%Y").date()
    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return dias[data.weekday()]

def dias_restantes_ano():
    """Calcula quantos dias faltam para o final do ano"""
    hoje = date.today()
    fim_ano = date(hoje.year, 12, 31)
    return (fim_ano - hoje).days
