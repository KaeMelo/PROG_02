class Pessoa:
    def __init__(self, nome, idade, cep, rua, tipo_sanguinio = None):
        self.nome = nome
        self.idade = idade
        self.cep = cep
        self.rua = rua
        self.tipo_sanguinio = tipo_sanguinio

    def alterar_cep(self, novo_CEP):
        self.cep = novo_CEP

    def alterar_rua(self, nova_rua):
        self.rua = nova_rua

Pessoa1 = Pessoa("Kae", "20", "55292262", "Luis Burgos", "o+")

Pessoa1.alterar_cep("55555555")
Pessoa1.alterar_rua("Boa Vista")

print(Pessoa1.cep)
print(Pessoa1.rua)