from cinema import Cinema

class Estreia:
    def _init_(self, cinema, titulo, em_cartaz, data_estreia):
        self._cinema = cinema
        self.titulo = titulo
        self.em_cartaz = em_cartaz
        self.data_estreia = data_estreia
    
    def listar_estreia(self, idcinema, titulo, data_estreia):
        if idcinema == self.cinema._id and titulo == self.titulo and data_estreia == self.data_estreia:
            return f"{self.titulo} Em cartaz no Cinema: {self.cinema._id} {self.cinema._nome} A partir de: {self.data_estreia}"
        else:
            return f"Que tal? {self.titulo} No cinema: {Cinema} Em: {data_estreia}"
