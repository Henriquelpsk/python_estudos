from programa import *

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
shrek = Filme("shrek 3", 2002, 120)
twd = Serie("the walking dead", 2010, 9)

vingadores.dar_like()
atlanta.dar_like()

lista_de_programas = [vingadores,atlanta,shrek,twd]
playlist_de_ferias = Playlist("Férias", lista_de_programas)

print(playlist_de_ferias[0])