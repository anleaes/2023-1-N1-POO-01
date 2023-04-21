class Sala:
    
    def __init__(self, num_sala, capacidade, assentos):
        self._num_sala = num_sala
        self._capacidade = capacidade
        self._assentos = assentos
        assentos = [False]*30 #inicializa um array com 30 posicoes com false
       
        def reservar_assento(self, assentos):
         if self._assentos[assentos]:
            return False
         else:
            self._assentos[assentos] = True
            return True

    def buscar_asento_livre(self):
        for i in range(len(self._assentos)):
            if self._assentos[i] == False:
                return i
        return -1   