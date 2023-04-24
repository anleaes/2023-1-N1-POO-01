from sala import Sala

class Sessao:
     def __init__(self, data_sessao, hora_sessao, sala): 
       self._data_sessao = data_sessao
       self._hora_sessao = hora_sessao
       self._sala = sala       
      
       def sala_sessao(self, data_sessao):
           
           if data_sessao == self._data_sessao: 
            return f'A sala {self._sala._num_sala} tem sessao em {self._data_sessao} as {self._hora_sessao}'
           else:
            return f'Nao ha sessao na data escolhida.'  
          
       def situacao_sessao(self, data_sessao):  
           if data_sessao != self._data_sessao: 
            return f'Não há sessão nesta data.\n'
           for i in range(len(self._sala._assentos)):    
            if self._sala._assentos[i] == False: 
              return f'Segue com vendas abertas {self._sala._num_sala} em {self._data_sessao} as {self._hora_sessao}.'      
           return f'A disponibilidade da sessao da {self._sala._num_sala} em {self._data_sessao} as {self._hora_sessao} esta encerrada!'