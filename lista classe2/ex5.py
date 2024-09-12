class ContaCorrente:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return self.saldo
        else:
            print("Saldo insuficiente para sacar ", valor)
            return self.saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo


conta = ContaCorrente("kae", 1000)

print("Saldo após sacar 500:", conta.sacar(500))

print("Saldo após depositar 200:", conta.depositar(200))

print("Saldo após tentar sacar 800:", conta.sacar(800))
