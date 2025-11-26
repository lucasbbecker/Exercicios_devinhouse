def somar(a, b):
    """Retorna a soma de dois números"""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números"""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números"""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números, com tratamento de erro"""
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b
