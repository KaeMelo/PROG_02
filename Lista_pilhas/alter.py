class Pilha:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def retirar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

def alternar_pilhas(pilha1, pilha2):
    pilha3 = Pilha()

    while not pilha1.esta_vazia() or not pilha2.esta_vazia():
        if not pilha1.esta_vazia():
            pilha3.adicionar(pilha1.retirar())
        if not pilha2.esta_vazia():
            pilha3.adicionar(pilha2.retirar())

    return pilha3


pilha1 = Pilha()
pilha2 = Pilha()


pilha1.adicionar(1)
pilha1.adicionar(2)
pilha1.adicionar(3)

pilha2.adicionar(4)
pilha2.adicionar(5)
pilha2.adicionar(6)


pilha3 = alternar_pilhas(pilha1, pilha2)

print("Elementos na Pilha 3:", pilha3.itens)

