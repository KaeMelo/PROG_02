numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1
    
print("Números no intervalo entre", numero1, "e", numero2, ":")
for i in range(numero1, numero2 + 1):
    print(i, end=" ")
