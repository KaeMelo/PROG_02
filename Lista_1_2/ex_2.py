def celsius_para_fahrenheit(celsius):
    if not isinstance (celsius, (int, float)):
        raise TypeError ("Digite apenas números: ")
    return (celsius * 9/5) + 32

try:
    celsius = float(input("Digite o valor em celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"{celsius} celsius em {resultado} fahrenheit: ")

except ValueError:
    print("ERROR: O valor digitado não é um número: ")