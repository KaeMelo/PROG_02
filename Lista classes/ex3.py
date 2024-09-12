class ContaCorrente:
    def __init__(self, nome, cliente, cpf, saldo_inicial, senha):
        self.nome = nome
        self.cliente = cliente
        self.cpf = cpf
        self.saldo = saldo_inicial
        self.senha = senha
        self.logged_in = False

    def fazer_login(self, cpf_digitado, senha_digitada):
        if cpf_digitado == self.cpf and senha_digitada == self.senha:
            self.logged_in = True
            return True
        else:
            return False
    
    def consultar_saldo(self):
        if self.logged_in:
            return self.saldo
        else:
            return "Faça login para consultar saldo"
        
    def realizar_deposito(self, valor):
        if self.logged_in:
            self.saldo += valor
            return self.saldo 
        else:
            "Faça login para reslizar deposito"

    def realizar_saque(self, valor):
        if self.logged_in:
            if valor > self.saldo:
                return "Saldo insuficiente"
            else:
                self.saldo -= valor
                return self.saldo
        else:
            return "Faça login para realizar saque"
        
    def fazer_logout(self):
        self.logged_in = False
        return "Logout feito com sucesso"

conta = ContaCorrente("Kae", "123456789", 1000.0, "senha123")

print(conta.fazer_login("123456789", "Senha123"))

print(conta.consultar_saldo())

print(conta.realizar_deposito())

print(conta.realizar_saque())

print(conta.fazer_logout())