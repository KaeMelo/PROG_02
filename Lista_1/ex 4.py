def encontrar_maior_numero(lista_numeros):
    maior_numero = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior = encontrar_maior_numero(numeros)

print("O maior número é:", maior)