def contaVogais(texto):
    contagem_vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    texto = texto.lower()

    for caractere in texto:
        if caractere in contagem_vogais:
            contagem_vogais[caractere] += 1

    return contagem_vogais

texto = "Aqui está."
resultado = contaVogais(texto)
print(resultado)
