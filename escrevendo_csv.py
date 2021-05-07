"""
#writer and writerow

from csv import writer

with open('filmes.csv', 'w') as file:
    writer_csv = writer(file)
    film = None
    writer_csv.writerow(['Title', 'Theme', 'Duration'])
    while film != 'stop':
        film = input('Title name: ')
        if film != 'stop':
            theme = input('Inform the theme: ')
            duration = input('Inform the duration: ')
            writer_csv.writerow([film, theme, duration])
"""


# Dictwriter

from csv import DictWriter

with open('filmes3.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writerow()
    filme = None
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            genero = input('Digite o genero do filme: ')
            duracao = input('Digite a duração do filme em minutos: ')
            escritor_csv.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})



