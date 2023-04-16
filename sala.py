class Sala:
    
    def __init__(self, num_sala, capacidade, assentos, ocupacao):
        self._num_sala = num_sala
        self._capacidade = capacidade
        self._assentos = assentos
        self._ocupacao = ocupacao
        
        def alocacao_vendas(self, assentos, ocupacao):    
            if self._ocupacao:
             return f'Assento {self._assento} Vendido!'
            else:
             return f'Assento {self._assento} Disponivel.'
        
        def capacidade_salas(self, num_sala, capacidade):
            return f'A {self._num_sala} tem capacidade de {self._capacidade}'       

