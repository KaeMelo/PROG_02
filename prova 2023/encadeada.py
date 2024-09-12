class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def contar_maiores_que(self, valor):
        atual = self.cabeca
        contador = 0
        while atual:
            if atual.valor > valor:
                contador += 1
            atual = atual.proximo
        return contador

    def contar_nos_pares(self):
        atual = self.cabeca
        contador = 0
        while atual:
            if atual.valor % 2 == 0:
                contador += 1
            atual = atual.proximo
        return contador

    def contar_nos_impares(self):
        atual = self.cabeca
        contador = 0
        while atual:
            if atual.valor % 2 != 0:
                contador += 1
            atual = atual.proximo
        return contador

    def mais_pares_ou_impares(self):
        pares = self.contar_nos_pares()
        impares = self.contar_nos_impares()
        if pares > impares:
            return "Mais números pares", pares - impares
        elif impares > pares:
            return "Mais números ímpares", impares - pares
        else:
            return "Mesma quantidade de pares e ímpares", 0

# Exemplo de uso
lista = ListaEncadeada()
lista.adicionar(1)
lista.adicionar(4)
lista.adicionar(3)
lista.adicionar(6)
lista.adicionar(7)

print("Quantidade de elementos maiores que 3:", lista.contar_maiores_que(3))
print("Quantidade de nós pares:", lista.contar_nos_pares())
print("Quantidade de nós ímpares:", lista.contar_nos_impares())
print(lista.mais_pares_ou_impares())
