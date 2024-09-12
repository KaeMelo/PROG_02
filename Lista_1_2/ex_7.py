def solicitar_numero():
    while True:
        try:
            numero = float(input("Digite um valor entre 0 e 10: "))
            if 0 <= numero <= 10:
                return numero
            else:
                print("O valor deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

numero = solicitar_numero()

print("Número válido inserido:", numero)