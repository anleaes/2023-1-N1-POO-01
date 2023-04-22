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

//Nessa implementação, temos a classe Loja com os atributos privados itens, preco e nota_fiscal,
e um construtor que recebe esses atributos como argumentos. O método compra permite que o cliente 
realize uma compra, atualizando os valores dos atributos da instância e retornando uma mensagem 
informando a nota fiscal da compra. O método tabela_precos recebe uma lista de itens e uma lista de
preços, e retorna um dicionário que mapeia cada item ao seu respectivo preço.