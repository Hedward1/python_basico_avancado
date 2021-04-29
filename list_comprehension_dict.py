"""
Dictionary Comprehension

lista = [1, 2, 3, 4] # list
tupla = 1, 2, 3, 4 # tuple
consjunto = {1, 2, 3, 4} # set
dicionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4} # dictionary

# Sintax

{chave:valor for valor in iterável}
[lista for valor in iterável]

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# exe lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
"""




