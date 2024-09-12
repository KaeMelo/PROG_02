def decompor_numero(numero):
    if not 0 < numero < 1000:
        raise ValueError("O número deve ser menor que 1000.")
    
    centenas = numero // 100
    resto = numero % 100
    dezenas = resto // 10
    unidades = resto % 10

    return centenas, dezenas, unidades

try:
    numero = int(input("Digite um número menor que 1000: "))

    centenas, dezenas, unidades = decompor_numero(numero)

    print(f"Centenas: {centenas}")
    print(f"Dezenas: {dezenas}")
    print(f"Unidades: {unidades}")
    
except ValueError:
    print("Erro: Por favor, insira um número válido menor que 1000.")
