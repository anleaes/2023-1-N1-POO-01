class Sala:
    
    def __init__(self, num_sala, capacidade, assentos, ocupacao):
        self._num_sala = num_sala
        self._capacidade = capacidade
        self._assentos = assentos
        self._ocupacao = ocupacao
        
        def alocacao_vendas(self, assentos):                
            if assentos == self._assentos:
             if self._ocupacao == 1:
              return f'Assento {self._assento} Vendido!'
             else:
              return f'Assento {self._assento} Disponivel.'
            else:
              return f'Assento inexistente.'
            
        def capacidade_salas(self, num_sala):
            if num_sala == self._num_sala:
             return f'A {self._num_sala} tem capacidade de {self._capacidade}'       
            else:
             return f'Sala inexistente.'   
