class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    def __str__(self):
        return f'{self.__nome} - {self.ano} - {self.__likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self.nome} Ano: {self.ano} Duração: {self.duracao}m Likes: {self.likes}"


class Serie(Programa):
    def __init__(self,nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self.nome} Ano: {self.ano} Temporadas: {self.temporadas} Likes: {self.likes}"


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
