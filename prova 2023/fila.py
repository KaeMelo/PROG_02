class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        else:
            return None

    def tamanho(self):
        return len(self.itens)

    def __str__(self):
        return str(self.itens)

def intercalar_filas(fila1, fila2):
    fila_combinada = Fila()

    while not fila1.esta_vazia() or not fila2.esta_vazia():
        if not fila1.esta_vazia():
            fila_combinada.enfileirar(fila1.desenfileirar())
        if not fila2.esta_vazia():
            fila_combinada.enfileirar(fila2.desenfileirar())

    return fila_combinada

# Exemplo de uso:
fila1 = Fila()
fila1.enfileirar(1)
fila1.enfileirar(3)
fila1.enfileirar(5)

fila2 = Fila()
fila2.enfileirar(2)
fila2.enfileirar(4)
fila2.enfileirar(6)
fila2.enfileirar(7)
fila2.enfileirar(8)

fila_combinada = intercalar_filas(fila1, fila2)
print("Fila combinada:", fila_combinada)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8]
