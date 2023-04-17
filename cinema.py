class Cinema:

    def __init__(self, id, responsavel, cnpj, endereco, telefone, cep, email):
        self._id = id
        self._responsavel = responsavel
        self._cnpj = cnpj
        self._endereco = endereco
        self._telefone = telefone
        self._cep = cep
        self._email = email
        
    def escolher_cinema (self):
        return self._cep._endereco