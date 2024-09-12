class Pilha:
    def __init__(self, tamanho_maximo=10):
        self.itens = []
        self.tamanho_maximo = tamanho_maximo

    def adicionar(self, item):
        if len(self.itens) >= self.tamanho_maximo:
            return "Pilha atualmente cheia"
        self.itens.append(item)
        return f"Elemento {item} adicionado com sucesso"

    def retirar(self):
        if self.esta_vazia():
            print("Erro: A pilha está vazia. Não é possível remover um elemento.")
            return None
        return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

    def esta_cheia(self):
        return len(self.itens) >= self.tamanho_maximo

pilha = Pilha()


for i in range(1, 12):
    resultado = pilha.adicionar(i)
    print(resultado)


print("Elementos na pilha:", pilha.itens)
