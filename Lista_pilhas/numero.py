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

    def quantidade_elementos(self):
        if self.esta_vazia():
            return "A pilha está atualmente vazia"
        return len(self.itens)

pilha = Pilha()

pilha.adicionar(1)
pilha.adicionar(2)
pilha.adicionar(3)

print("Quantidade de elementos na pilha:", pilha.quantidade_elementos())  # Saída: 3

pilha.retirar()
pilha.retirar()
pilha.retirar()

print("Quantidade de elementos na pilha:", pilha.quantidade_elementos())  # Saída: A pilha está atualmente vazia
