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
        return self._nome._endereco
        print ("Você selecionou o Cinema")
    
