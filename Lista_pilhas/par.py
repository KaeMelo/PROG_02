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
        return len(self.itens)

    def par_ou_impar(self):
        quantidade = self.quantidade_elementos()
        if quantidade == 0:
            return "A pilha está vazia."
        elif quantidade % 2 == 0:
            return "A pilha contém um número par de elementos."
        else:
            return "A pilha contém um número ímpar de elementos."


pilha = Pilha()


pilha.adicionar(1)
pilha.adicionar(2)
pilha.adicionar(3)

print(pilha.par_ou_impar())  


pilha.adicionar(4)


print(pilha.par_ou_impar())  

pilha.retirar()
pilha.retirar()
pilha.retirar()
pilha.retirar()


print(pilha.par_ou_impar())  
