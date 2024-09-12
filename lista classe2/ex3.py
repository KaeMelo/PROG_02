class Produto:
    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def retornar_nome(self):
        return self.nome

    def retornar_quantidade(self):
        return self.quantidade

    def retornar_preco_unitario(self):
        return self.preco_unitario

    def venda_produto(self, quantidade_desejada, valor_pago):
        if quantidade_desejada <= 0:
            print("Quantidade inválida. A quantidade deve ser maior que zero.")
            return
        if quantidade_desejada > self.quantidade:
            print("Quantidade insuficiente em estoque.")
            return
        valor_total = quantidade_desejada * self.preco_unitario
        if valor_pago < valor_total:
            print("Valor insuficiente. O valor pago deve ser igual ou maior que R$", valor_total)
            return
        troco = valor_pago - valor_total
        self.quantidade -= quantidade_desejada
        print("Venda realizada com sucesso!")
        print("Troco: R$", troco)


produto1 = Produto("Camiseta", 10, 25.00)

quantidade_desejada = int(input("Digite a quantidade desejada: "))
valor_pago = float(input("Digite o valor pago pelo cliente: "))

produto1.venda_produto(quantidade_desejada, valor_pago)

print("Quantidade em estoque após a venda:", produto1.retornar_quantidade())
