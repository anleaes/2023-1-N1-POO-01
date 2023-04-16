from sala import Sala

class Sessao:
    def __init__(self, data_sessao, hora_sessao, encerrada, num_sala, assentos, ocupacao):
       super().__init__(num_sala, assentos, ocupacao)
       self._num_sala = data_sessao
       self._assentos = hora_sessao
       self._ocupacao = encerrada
      
       def sala_sessao(self, data_sessao, hora_sessao, num_sala): 
           return f'A sala {self._num_sala} tem sessao em {self._data_sessao} as {self._hora_sessao}'
      
       def situacao_sessao(self, encerrada, data_sessao, hora_sessao, num_sala):   
           print('A disponibilidade da sessao da {self._num_sala} em {self._data_sessao} as {self.hora_sessao} esta')
           if encerrada:
              return f' encerrada!'
           else:
             return f' com vendas abertas.'
