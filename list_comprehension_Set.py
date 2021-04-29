"""
SET COMPREHENDION

lista = [1, 2, 3, 4] # list
tupla = 1, 2, 3, 4 # tuple
consjunto = {1, 2, 3, 4} # set
dicionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4} # dictionary


numeros = {num for num in range(1, 7)}
print(numeros)
"""



numeros = {x ** 2 for x in range(10)}
print(numeros)

#DESAFIO! OBS FAÇA UMA ALTERAÇÃO DA ESTRUTURA ACIMA PARA GERAR UM DICIONARIO AO INVEZ DE SET

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# finalizar com string
letras = {letra for letra in 'Geek University'}
print(letras)
