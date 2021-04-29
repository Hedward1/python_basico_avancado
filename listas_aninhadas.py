"""
Litas Aninhadas

numeros = [1, 2, 3, 4, 5]

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(listas)
print(type(listas))

#acessando dados

print(listas[0][1])  # 2
print(listas[2][1])  # 8

"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# iterando com loops em uma lista aninnhada

# for lista in listas:
#     #print(lista)
#     for numero in lista:
#         print(numero)

# # List Comprehension
#[print(valor) for valor in listas]
[[print(valor) for valor in lista] for lista in listas]


# gerando tabuleiro 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['x' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]

print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)]for j in range(1, 4)])

