class Filme:
        def __init__(self, titulo: str, duracao: str, genero: str, classificacao: str):
        self.titulo = nome
        self.duracao = duracao
        self.genero = genero
        self.classificacao = classificacao
        
    def get_filme(self):
        return self.titulo + " - " + self.genero + " - " + self.duracao + " - " + self.classificacao