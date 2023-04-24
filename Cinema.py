class Cinema:

    def _init_(self, id, nome, cnpj, endereco, telefone, cep, email):
        super().__init__(nome, endereco)
        self._id = id
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco
        self._telefone = telefone
        self._cep = cep
        self._email = email
    
    def selecionar_cinema(self):
        return f"{self._id} Nome: {self._nome} Localização: {self._endereco}"
    
