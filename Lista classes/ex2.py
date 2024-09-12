class Aluno:
    def __init__(self, nome, cpf, dia_nascimento, mes_nascimento, ano_nascimento, endereco, curso):
        self.nome = nome
        self.cpf = cpf
        self.dia_nascimento = dia_nascimento
        self.mes_nascimento = mes_nascimento
        self.ano_nascimento = ano_nascimento
        self.endereco = endereco
        self.curso = curso

    def calcular_idade(self):
        idade = 2024 - self.ano_nascimento
        return idade
    
    def mostrar_endereco(self):
        return self.endereco

    def retornar_curso(self):
        return self.curso

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso

    def alterar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def gerar_matricula(self, codigo_disci):
        matricula = str(self.ano_nascimento) + self.cpf[:6] + codigo_disci
        return matricula
    
Aluno1 = Aluno("Kae", "123456789", 6, 3, 20, "Rua Luis", "Engenharia Eletrica")

print("Idade:", Aluno1.calcular_idade())

print("Endereço:", Aluno1.mostrar_endereco())

Aluno1.alterar_curso("Engenharia de software")
print("Novo curso:", Aluno1.retornar_curso())

Aluno1.alterar_endereco("Boa vista")
print("Novo endereço:", Aluno1.mostrar_endereco())

print("Matricula:", Aluno1.gerar_matricula("001"))