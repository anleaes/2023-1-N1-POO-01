class Loja:
    def __init__(self, nota_fiscal, itens, preco):
    self.itens = itens
    self.preco = preco
    self.nota_fiscal = nota_fiscal

    def compra(self, nota_fiscal, itens, preco):
    self.itens = itens
    self.preco = preco
    self.nota_fiscal = nota_fiscal
    return f"Compra realizada com sucesso. Nota Fiscal: {self.nota_fiscal}"

    def tabela_precos(self, itens, preco):
    tabela = {}
    for i in range(len(itens)):
        tabela[itens[i]] = preco[i]
    return tabela
