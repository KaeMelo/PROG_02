class Aluno:
    def __init__(self, nome, cpf, ano_nascimento, mes_nascimento, dia_nascimento, curso):
        self.nome = nome
        self.cpf = cpf
        self.ano_nascimento = ano_nascimento
        self.mes_nascimento = mes_nascimento
        self.dia_nascimento = dia_nascimento
        self.curso = curso

    def retornar_nome(self):
        return self.nome

    def retornar_cpf(self):
        return self.cpf

    def retornar_ano_nascimento(self):
        return self.ano_nascimento

    def retornar_mes_nascimento(self):
        return self.mes_nascimento

    def retornar_dia_nascimento(self):
        return self.dia_nascimento

    def retornar_curso(self):
        return self.curso

    def modificar_nome(self, novo_nome):
        self.nome = novo_nome

    def modificar_curso(self, novo_curso):
        self.curso = novo_curso

    def gerar_matricula(self):
        ano_atual = self.obter_ano_atual()
        matricula = self.nome[:3] + self.curso[:3] + str(ano_atual)
        return matricula

    def obter_ano_atual(self):
        data_atual = self.obter_data_atual()
        return data_atual.year

    def obter_data_atual(self):
        return self.obter_data_especifica()

    def obter_data_especifica(self):
        import time
        data_atual = time.localtime()
        return data_atual


aluno1 = Aluno("kae", "123.456.789-00", 1998, 5, 15, "Engenharia")
print("Matrícula de", aluno1.retornar_nome(), ":", aluno1.gerar_matricula())
print("Curso de", aluno1.retornar_nome(), ":", aluno1.retornar_curso())

aluno1.modificar_nome("Santos")
aluno1.modificar_curso("Ciência da Computação")
print("Novo nome:", aluno1.retornar_nome())
print("Novo curso:", aluno1.retornar_curso())
print("Nova matrícula:", aluno1.gerar_matricula())