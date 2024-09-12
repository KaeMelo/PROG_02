def calcular_salario(horas_por_hora, horas_trabalhadas):
    salario_bruto = horas_por_hora * horas_trabalhadas
    inss = salario_bruto * 0.08
    ir = salario_bruto * 0.11
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - inss - ir - sindicato
    return salario_bruto, inss, ir, sindicato, salario_liquido

try:
    valor_por_hora = float(input("Quanto você ganha por hora? "))
    horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

    salario_bruto, inss, ir, sindicato, salario_liquido = calcular_salario(valor_por_hora, horas_trabalhadas)

    print(f"+ Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"- IR (11%): R$ {ir:.2f}")
    print(f"- INSS (8%): R$ {inss:.2f}")
    print(f"- Sindicato (5%): R$ {sindicato:.2f}")
    print(f"= Salário Líquido: R$ {salario_liquido:.2f}")
    
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos.")