class Filme:
        def __init__(self, nome: str, duracao: str, genero: str, classificacao: str):
        self.nome = nome
        self.duracao = duracao
        self.genero = genero
        self.classificacao = classificacao
        
    def get_filme(self):
        return self.nome + " - " + self.genero + " - " + self.duracao + " - " + self.classificacao