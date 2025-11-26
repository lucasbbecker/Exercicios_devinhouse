def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


def maior_e_menor(lista):
    if len(lista) == 0:
        return None, None
    return max(lista), min(lista)


def main():
    print("=== Verificar Maior e Menor Número da lista! ===\n")
    
    numeros_str = input("Digite uma lista de números separados por espaço: ")
    
    numeros = [float(n) for n in numeros_str.split()]
    
    maior, menor = maior_e_menor(numeros)
    
    print("\nResultados:")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    

if __name__ == "__main__":
    main()
