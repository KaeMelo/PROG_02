class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            return None

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            return None

    def tamanho(self):
        return len(self.itens)

    def __str__(self):
        return str(self.itens)

def reverter_pilha(pilha):
    pilha_temp = Pilha()
    while not pilha.esta_vazia():
        pilha_temp.empilhar(pilha.desempilhar())
    return pilha_temp

def remover_numeros_pares(pilha):
    pilha_temp = Pilha()
    while not pilha.esta_vazia():
        topo = pilha.desempilhar()
        if topo % 2 != 0:
            pilha_temp.empilhar(topo)
    # Reverter a pilha para manter a ordem original dos ímpares
    pilha_revertida = reverter_pilha(pilha_temp)
    return pilha_revertida

# Exemplo de uso:
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)

print("Pilha original:", pilha)  # Saída: [1, 2, 3, 4, 5]

pilha_revertida = reverter_pilha(pilha)
print("Pilha revertida:", pilha_revertida)  # Saída: [5, 4, 3, 2, 1]

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
pilha.empilhar(5)

pilha_impares = remover_numeros_pares(pilha)
print("Pilha apenas com ímpares:", pilha_impares)  # Saída: [1, 3,
