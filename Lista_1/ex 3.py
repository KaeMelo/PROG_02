def numeros_pares_ate_n(n):
    lista_pares = []
    for i in range(2, n + 1, 2):
        lista_pares.append(i)
    return lista_pares

n = int(input("Digite um número inteiro: "))

pares = numeros_pares_ate_n(n)

print("Números pares até", n, ":", pares)