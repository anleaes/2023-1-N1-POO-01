class Filme:
    def __init__(self, titulo, genero, duracao, classificacao, em_cartaz):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.classificacao = classificacao
        self.em_cartaz = em_cartaz

    def listar_filmes(self, titulo, em_cartaz):
        if self.em_cartaz == em_cartaz:
            return self.titulo
        else:
            return "Filme não está em cartaz."

    def classificacao(self, titulo, classificacao):
        if self.titulo == titulo:
            self.classificacao = classificacao
            return "Classificação atualizada com sucesso."
        else:
            return "Filme não encontrado."
