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

    def remover_especifico(self, item):
        if self.esta_vazia():
            print("Erro: A pilha está vazia. Não é possível remover o elemento específico.")
            return None

        temp_pilha = Pilha()
        encontrado = False

        while not self.esta_vazia():
            topo = self.retirar()
            if topo == item:
                encontrado = True
                break
            temp_pilha.adicionar(topo)

        while not temp_pilha.esta_vazia():
            self.adicionar(temp_pilha.retirar())

        if not encontrado:
            print(f"Erro: O elemento '{item}' não foi encontrado na pilha.")
        else:
            print(f"O elemento '{item}' foi removido da pilha.")

pilha = Pilha()
pilha.adicionar(1)
pilha.adicionar(2)
pilha.adicionar(3)

print("Elemento removido:", pilha.retirar())  
print("A pilha está vazia?", pilha.esta_vazia()) 

pilha.remover_especifico(2)  
pilha.remover_especifico(5) 

print("Elemento removido:", pilha.retirar())  
print("A pilha está vazia?", pilha.esta_vazia())  
