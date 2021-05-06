"""
Lendo CSV

# virgula
1, 2, 3, 4, 5, 6,

"geek", "university", "python", 'ciencia', "dados"

# ponto e virgula

1; 2; 3; 4; 5;

# espaço
1 2 3 4 5 6

# não é ideal trabalhar com csv, fica trabalhoso
with open('lutadores.csv', encoding='utf-8')as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2]
    print(dados)

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # pula a primeira linha, no caso cabeçalho
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]}, nasceu no(a) {linha[1]} e mede {linha[2]} em centimetros')

#DictReader
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f'{linha[" Nome"]}, nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]}')

"""
#DictReader
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')     #caso queira especificar um delimitardor mudar a ","
                                                        # (que já é padronizando)
    for linha in leitor_csv:
        print(f'{linha[" Nome"]}, nasceu no(a) {linha["País"]} e mede {linha["Altura (em cm)"]}')


