from datetime import datetime, date

data_str = input("Digite uma data no formato DD/MM/AAAA: ")

try:
    data_usuario = datetime.strptime(data_str, "%d/%m/%Y").date()
except ValueError:
    print("Formato inválido! Use DD/MM/AAAA.")
    exit()

ultimo_dia_ano = date(data_usuario.year, 12, 31)
dias_restantes = (ultimo_dia_ano - data_usuario).days

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
dia_semana = dias_semana[data_usuario.weekday()]


print("\nData informada:", data_usuario.strftime("%d/%m/%Y"))
print("Dia da semana:", dia_semana)
print("Dias restantes para o final do ano:", dias_restantes)
