def ordem_crescente(num1, num2, num3):
    if not all(isinstance(num, (int, float)) for num in [num1, num2, num3]):
        raise TypeError("Todos os parâmetros devem ser números.")
    
    numeros = [num1, num2, num3]
    numeros.sort()

    return numeros

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    resultado = ordem_crescente(num1, num2, num3)

    print("Números em ordem crescente:", resultado)

except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")
