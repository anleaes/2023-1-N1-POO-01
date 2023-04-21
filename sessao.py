from sala import Sala

class Sessao:
    def __init__(self, data_sessao, hora_sessao, num_sala, assentos):
       super().__init__(num_sala, assentos)
       self._data_sessao = data_sessao
       self._hora_sessao = hora_sessao       
      
       def sala_sessao(self, data_sessao):
           
           if data_sessao == self._data_sessao: 
            return f'A sala {self._num_sala} tem sessao em {self._data_sessao} as {self._hora_sessao}'
           else:
             return f'Nao ha sessao na data escolhida.'  
          
       def situacao_sessao(self, data_sessao):  
           for self in self.assentos:
            if data_sessao == self._data_sessao: 
                if self._assentos == [True]: 
                 return f'A disponibilidade da sessao da {self._num_sala} em {self._data_sessao} as {self.hora_sessao} esta encerrada!'
                else:
                 return f'Segue com vendas abertas {self._num_sala} em {self._data_sessao} as {self.hora_sessao}.'