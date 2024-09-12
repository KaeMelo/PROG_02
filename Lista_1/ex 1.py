def comparar_numeros(a, b):
    if a == b:
        print("Os números são iguais")
    elif a > b:
        diferenca = abs(a - b)
        print(f"O número {a} é maior que o número {b} em {diferenca} unidades")
    else:
        diferenca = abs(a - b)
        print(f"O número {b} é maior que o número {a} em {diferenca} unidades")

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

comparar_numeros(numero1, numero2)