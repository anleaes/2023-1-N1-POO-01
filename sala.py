class Sala:
    
    def __init__(self, num_sala, capacidade):
        self._num_sala = num_sala
        self._capacidade = capacidade
        self._assentos = [False]*30 #inicializa um array com 30 posicoes com false
       
    def reservar_assento(self, assento):
      if self._assentos[assento-1]:
        return False
      else:
        self._assentos[assento-1] = True
        return True

    def buscar_assento_livre(self):
      for i in range(len(self._assentos)):
        if self._assentos[i] == False:
          return i+1
      return -1   