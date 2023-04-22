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

//Nessa implementação, temos a classe Filme com os atributos privados titulo, genero, duracao,classificacao e em_cartaz, e um construtor que recebe esses atributos como argumentos. O método listar_filmes recebe como parâmetros um título e um booleano que indica se o filme está em cartaz ou não, e retorna o título do filme se ele estiver em cartaz ou uma mensagem informando que 
o filme não está em cartaz. O método classificacao recebe como parâmetros um título e uma classificação indicativa e atualiza a classificação do filme correspondente se ele for encontrado, ou retorna uma
mensagem informando que o filme não foi encontrado. 