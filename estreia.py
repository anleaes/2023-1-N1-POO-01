class Estreia:
    def _init_(self, id, titulo, em_cartaz, data_estreia):
        self.id = Cinema
        self.titulo = titulo
        self.em_cartaz = em_cartaz
        self.data_estreia = data_estreia
    
    def listar_estreia(self, Cinema, titulo, data_estreia):
        if Cinema == self.id and titulo == self.titulo and data_estreia == self.data_estreia:
            return f"{self.titulo} Em cartaz no Cinema: {self.id} A partir de: {self.data_estreia}"
        else:
            return f"{self.titulo} Estreia: {Cinema} Em: {data_estreia}"
