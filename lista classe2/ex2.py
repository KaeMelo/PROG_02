class Funcionario:
    def __init__(self, nome, matricula, salario, login, senha):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.login = login
        self.senha = senha
        self.logado = False

    def retornar_nome(self):
        return self.nome

    def retornar_matricula(self):
        return self.matricula

    def retornar_salario(self):
        return self.salario

    def retornar_login(self):
        return self.login

    def retornar_senha(self):
        return self.senha

    def login(self, login_digitado, senha_digitada):
        if login_digitado == self.login and senha_digitada == self.senha:
            self.logado = True
            return True
        else:
            return False

    def estarLogado(self):
        return self.logado


funcionario1 = Funcionario("kae", "12345", 2500, "kae123", "senha123")

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if funcionario1.login(login, senha):
    print("Login realizado com sucesso!")
else:
    print("Login e/ou senha incorretos. Login não realizado.")

print("O funcionário está logado? ", funcionario1.estarLogado())
