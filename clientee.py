from loja import Loja
from ingresso import Ingresso

class Cliente:
  
    def __init__(self, nome, cpf, data_nascimento, telefone, email, loja, ingresso):   
       self._nome = nome
       self._cpf = cpf
       self._data_nascimento = data_nascimento
       self._telefone = telefone
       self._email = email
       self._loja = loja
       self._ingresso = ingresso
      
    def contato_cliente(self):
       print(f'Segue: {self._nome}, {self._telefone}, {self._email}')
        
    def consumo_cliente(self):
       print(f'Segue: {self._nome}, {self._email}, {self._ingresso._id}, {self._loja.nota_fiscal}')