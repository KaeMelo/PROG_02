def metros_para_centimetros(metros):
    if not isinstance (metros, (int, float)):
        raise TypeError ("Digite apenas números: ")
    return metros * 100

try:
    metros = float(input("Digite o valor em metros: "))
    resultado = metros_para_centimetros(metros)
    print(f"{metros} metros em {resultado} centimetros: ")

except ValueError:
    print("ERROR: O valor digitado não é um número: ")