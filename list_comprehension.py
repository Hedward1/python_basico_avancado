"""
List Comprehension

- Podemos gerar novas listas com dados processados a partir d eoutro iterável.

#sintaxe list comprehension

[ dado  for in iteravel ]

numeros = [ 1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in  numeros]
print(res)

# list compehension x loop
#loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero*2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#list compehensions
print([numero * 2 for numero in numeros])

"""

# outros exemplos:
#1
nome = [' Geek University']
print([letra.upper() for letra in nome])

#2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedroo', 'guilher', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])
#3
print([numero * 3 for numero in range(1, 10)])

#4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

#5
print([str(numero) for numero in range(1, 6)])


