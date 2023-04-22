class Ingresso:

    def __init__(self, tipo, id, preco_ingresso, sessao):
        self._tipo = tipo
        self._id = id
        self._preco_ingresso = preco_ingresso
        self._sessao = sessao

    def escolher_ingresso (self):
        return self._tipo_tipo