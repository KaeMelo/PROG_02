def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("O número deve ser não negativo.")
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Digite um número para calcular o fatorial: "))
    fatorial = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {fatorial}")

except ValueError:
    print("Erro: Por favor, insira um número inteiro.")