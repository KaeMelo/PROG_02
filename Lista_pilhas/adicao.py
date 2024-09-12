class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def retirar(self):
        if self.esta_vazia():
            print("Erro: A pilha está vazia. Não é possível remover um elemento.")
            return None
        return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

    def adicionar_pilha(self, outra_pilha):
        temp_pilha = Pilha()

        while not outra_pilha.esta_vazia():
            temp_pilha.adicionar(outra_pilha.retirar())

        while not temp_pilha.esta_vazia():
            self.adicionar(temp_pilha.retirar())


pilha1 = Pilha()
pilha2 = Pilha()

pilha1.adicionar(1)
pilha1.adicionar(2)
pilha2.adicionar(3)
pilha2.adicionar(4)

pilha1.adicionar_pilha(pilha2)

print("Elementos na Pilha 1 após adicionar Pilha 2:", pilha1.itens)
