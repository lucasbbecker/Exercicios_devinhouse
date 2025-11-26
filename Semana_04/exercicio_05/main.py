import funcoes_calculo as calc
import funcoes_data as data

def main():
    print("=== Sistema Modularizado ===\n")

    # Teste das funções matemáticas
    print("Operações matemáticas:")
    a, b = 10, 5
    print(f"{a} + {b} = {calc.somar(a, b)}")
    print(f"{a} - {b} = {calc.subtrair(a, b)}")
    print(f"{a} * {b} = {calc.multiplicar(a, b)}")
    print(f"{a} / {b} = {calc.dividir(a, b)}")

    # Teste das funções de data
    print("\nOperações com datas:")
    data_informada = "03/11/2025"
    print(f"Data informada: {data_informada}")
    print("Dia da semana:", data.dia_da_semana(data_informada))
    print("Dias restantes para o final do ano:", data.dias_restantes_ano())

# Execução principal
if __name__ == "__main__":
    main()
