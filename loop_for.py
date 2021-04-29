nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# for letra in nome:
#     print(letra)
#
# for numeros in lista:
#     print(numeros)
#
# for numeros in range(1, 10):
#     print(numeros)

# for i, letra in enumerate(nome):
#     print(i, letra, nome)

# for valor in enumerate(nome):
#     print(valor)

# qtd = int(input('Quantas vezes irá repetir esse loop ? \n'))
# soma = 0
#
# for n in range(1, qtd+1):
#     num = int(input(f'Informe o {n}/{qtd} valor: \n'))
#     soma += num
# print(f'A soma é {soma}')

# ORIGINAL:   U+1F60D
# MODIFICADO: U0001F605

x = 3

for _ in range(x):
    for numero in range(1, 11):
        print('\U0001F605' * numero)


