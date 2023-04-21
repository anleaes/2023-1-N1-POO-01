class filme:
    
    def __init__(self, titulo, genero, duracao, clasindicativa):
        
        self._titulo = titulo
        self._genero = genero
        self._duracao = duracao
        self._clasindicativa = clasindicativa
        
    def get_filme(self):
        return self.titulo + " - " + self.genero + " - " + self.duracao + " - " + self.clasindicativa