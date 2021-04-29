"""
Recebendo dados de usuário
"""
# Entrada de dados
#print("qual seu nome? ")
nome = input('Qual seu nome? ') # input = Entrada

# Processamento
print(f'Seja bem vindo(a) {nome}')
#print("qual sua idade? ")
idade = input('qual sua idade?')

print('A %s tem %s anos' % (nome, idade))
print('A {0} tem {1} anos'.format(nome, idade))
print(f'A {nome} tem {idade} anos')
"""
# int(idade) => cast
é converção de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2021 - int(idade)}')