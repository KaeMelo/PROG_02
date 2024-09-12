def verificar_genero(caractere):
    if caractere.upper() == "F":
        return "Feminino"
    elif caractere.upper() == "M":
        return "Masculino"
    else:
        return "Inválido"

caractere = input("Por favor, insira um caractere (F ou M): ")

resultado = verificar_genero(caractere)

print("Gênero:", resultado)