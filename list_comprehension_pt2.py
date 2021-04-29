"""
List comprehension
nós podemos adicionar estruturas condicionais lógicas
"""
#1
numeros = [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# refatorar
# qualquer numero par módulo de 2 é 0, e 0 em python é False. NOT FALSE= True
pares = [numero for numero in numeros if not numero % 2]
# qualquer numero impar módulo de 2 é 1, e 1 em python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

#2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]