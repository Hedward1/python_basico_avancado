"""
LISTAS

FUNCIONAM COMO VETORES/MATRIZES (ARRAYS) EM OUTRAS LINGUAGENS, COM A DIFERENÇA DE SEREM DINAMICOS E TAMBEM DE
PODERMOS COLOCAR QUALQUER TIPO DE DADO

Linguagens C/Java : Arrays
    -   Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será sempre do tipo
    inteiro e poderá ter SEMPRE no máximo 5 valores
Já em Python:

    - Dinâmico: Não possue tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
    - Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado.
As listas em python são representadas por '[]'

# Podemos chegar se determinaod valor está contido na lista
num = 4
if num in lista1: # serve tambem para o range(lista4)
    print(f'Encontrei o numero {num}')
else:
    print(f'não encontrei o numero {num}')

# # Contagem:
# caractere = 'e'
# contagem = 0
# for letra in lista5:
#     if letra == caractere.lower() or letra == caractere.upper():
#         contagem += 1
#
# print(f'Total de letras "{caractere}" são: {contagem}')
#
# # ou podemos usar
# print(f'contagem do caractere "e": {lista5.count(caractere)}')

# # Odenar lista
# lista1.sort()
# print(lista1)
# print(lista1)
#
# lista2.sort()
# print(lista2)
# lista2.sort(reverse=True)
# print(lista2)

#adiciona elemento um por vez.
lista1.append(42) # adiciona valor numa lista, e apenas um item

lista6 = [4, 5, 55]
lista7 = [122, 159, 147]
lista1.append(lista6)# cria uma sublista

print(f'lista1.append({lista1})')
print(lista1.extend(lista7))
print(f'lista1.extend({lista1})')

# Pode ser inserido um novo elemento na lista, informando a osição do índice
lista1.insert(2, 'Novo Valor')
print(lista1)

# Pode ser inserido um novo elemento na lista, informando a osição do índice
lista1.insert(2, 'Novo Valor')
print(lista1)

lista6 = lista1 + lista2
print(lista6)
# copia de uma lista para uma variável
lista6 = lista2.copy()
print(lista6)

# podemos contar quantos elmentos existem dentro da lista
print(len(lista5))

# Podemos remover elementos do ultimo indice de uma lista
# Os elementos a direita serão deslocados para esquerda
print(lista5)
print(lista5.pop())
lista5.pop()
print(lista5)
print(lista5.pop(3))

# Podemos repetir elementos em uma lista
lista1 *= 3
print(lista1)

# Converter String em lista,
string1 = 'Geek,University,é,Legal'
print(type(string1))
lista5 = string1.split(',')
print(lista5)

# Convertendo uma lista em uma string.
lista6 = ['Geek', 'University', 'é', 'Legal']
print(lista6)
# pega a lista 6 e colcoa espaçoes entre gada elemto e transforma em uma string
curso = ' '.join(lista6)
print(curso)
# em vez do espaço podemos colocar algum outro caractere
curso = '$'.join(lista6)
print(curso)

#pode ser colocado qualquer tipo de dato em lista, inclusive misturando dados
lista6 = [1, 1.57, True, 'Geek', 'd', [1, 2, 3], 3423444545]
print(lista6)
print(dir(lista6))

# Iterando sobre listas
# Exe - 01 FOR
soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma+elemento
print(soma)


# Exe - 02 WHILE

carrinho = []
produto = ''

while produto != 'Sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input().title()
    if produto != 'Sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#aceso aos elementos de forma indexada

cores = ['azul', 'amarelo', 'preto', 'rosa', 'vermelho', 'verde', 'branco']

for cor in cores:
    print(cor)

# Gerar indice em um for
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

for indice, cor in enumerate(cores):lista_competidores
    print(indice, cor)

print(list(enumerate(cores)))

# Outros metodos
# Encontrar index de um elemento na lista

numeros = [5, 6, 7, 8, 9, 10]
print(numeros.index(6))

print(numeros.index(9))
# Dentro de um range
print(numeros.index(8, 3, 6)) # Busca o indice do valor 8, entre 3 e 6

# # Copiando uma lista para outra (Shallow Copy e Deep Copy)
# lista = [1, 2, 3]
# print(lista)
# nova = lista.copy() # copia
#
# print(nova)
# nova.append(4)
# print(lista)
# print(nova)

# lista.copy() não mudam seus valores, ficando idependente, tambem conhecido como Deep Copy

# abaixo itulizamos copia via tribuição, copiando de lista para nova, mas appós modificar uma mda
# as duas, tambem conhecido como Shallow Copy


lista01 = [1, 2, 3]
nova01 = lista01 #copia
print(nova01)

nova01.append(4)
print(lista01)
print(nova01)
"""

lista1 = [1, 99, 4, 27, 15]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University é Legal')
cores = ['azul', 'amarelo', 'preto', 'rosa', 'vermelho', 'verde', 'branco']

