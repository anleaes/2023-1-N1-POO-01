from ingresso import Ingresso
from sala import Sala

class Cliente:
    def __init__(self, nome, cpf, data_nascimento, telefone, email, tipo, id, preco_ingresso, itens, preco, nota_fiscal):
       super().__init__(tipo, id, preco_ingresso, itens, preco, nota_fiscal)
       self._nome = nome
       self._cpf = cpf
       self._data_nascimento = data_nascimento
       self._telefone = telefone
       self._email = email
    
    def contato_cliente(self, nome, telefone, email):
        set(self._nome, self._telefone, self._email)
        
    def consumo_cliente(self, nome, email, ingresso, compras):
        return self._nome, self._email, self._ingresso, self._compras