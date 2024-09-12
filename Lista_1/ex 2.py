def verificar_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"
    
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

resultado = verificar_aprovacao(nota1, nota2)
print("O aluno está", resultado)
