class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerdo = None
        self.direito = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if chave < no.chave:
            if no.esquerdo is None:
                no.esquerdo = No(chave)
            else:
                self._inserir(no.esquerdo, chave)
        else:
            if no.direito is None:
                no.direito = No(chave)
            else:
                self._inserir(no.direito, chave)

    def _eh_primo(self, numero):
        if numero <= 1:
            return False
        if numero == 2:
            return True
        if numero % 2 == 0:
            return False
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

    def contar_chaves_primas(self):
        return self._contar_chaves_primas(self.raiz)

    def _contar_chaves_primas(self, no):
        if no is None:
            return 0
        contador = 0
        if self._eh_primo(no.chave):
            contador += 1
        contador += self._contar_chaves_primas(no.esquerdo)
        contador += self._contar_chaves_primas(no.direito)
        return contador

    def contar_filhos(self, no):
        if no is None:
            return 0
        return 1 + self.contar_filhos(no.esquerdo) + self.contar_filhos(no.direito)

    def comparar_filhos_esquerdo_direito(self):
        if self.raiz is None:
            return "Árvore vazia", 0
        filhos_esquerdo = self.contar_filhos(self.raiz.esquerdo)
        filhos_direito = self.contar_filhos(self.raiz.direito)
        if filhos_esquerdo > filhos_direito:
            return "Mais filhos à esquerda", filhos_esquerdo - filhos_direito
        elif filhos_direito > filhos_esquerdo:
            return "Mais filhos à direita", filhos_direito - filhos_esquerdo
        else:
            return "Mesma quantidade de filhos", 0

# Exemplo de uso
arvore = ArvoreBinariaBusca()
chaves = [10, 5, 15, 3, 7, 12, 17, 2, 8, 11, 13]
for chave in chaves:
    arvore.inserir(chave)

print("Quantidade de chaves com valor primo:", arvore.contar_chaves_primas())
print(arvore.comparar_filhos_esquerdo_direito())
