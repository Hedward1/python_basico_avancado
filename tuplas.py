"""
        TUPLAS
1 - Representadas por ()
2 - São imutáveis

---

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# tuplas com 1 elemento não são tuplas
tupla3 = (4)
print(tupla3)
print(type(tupla3))

# Agora é uma tupla
tupla4 = (4,)
print(tupla4)
print(type(tupla4))

tupla5 = 5, [2, 5, 6]
print(tupla5)
print(type(tupla5))

#    tuplas são definidads pela ',' e não pelo '()'
(4) Não é tupla
(4,) tupla
4, tupla

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tuplas

tupla = ('Geek university', 'Programação em Python')
escola, curso = tupla
print(escola)
print(curso)

# métodos de Adição/Remoção de valores na stuplas não existem.

tupla1 = 1, 2, 3
tupla2 = 4, 5, 6
tupla3 = tupla1 + tupla2
print(tupla3)
#ou
tupla1 += tupla2
print(tupla1)

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

tupla = 1, 2, 3

print(3 in tupla)


#Iterando sobre uma tupla
tupla = 1, 2, 3

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contagem de elementos na tupla

tupla = 'a', 'b', 'c', 'd', 'e', 'a', 'b'

print(tupla.count('a'))
escola = tuple('Geek University')
print(escola)
print(escola.count('e'))


# Dicas na utilização de tuplas

# Devemos usar tuplas sempre que não precisamos usar dados contidos em uma coleção
# Exemplo 1
meses = 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Desembro'
# meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Desembro']
#meses.append('Playstation')
# i = 0
# while i < len(meses):
#     print(meses[i])
#     i = i + 1

data = 'junho'
print(meses.index(data.title()))
# obs caso o elemento não ecista será gerado erro
# como criei messes com o primeira maiúscula, o .tittle() será necessário.

# slicing
print(meses[5:])

# PQ usar tuplas ?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam o código mais seguro*.

# * Trabalahar com elementos imutáveis traz mais segurança para o código

# Copiando um tupla para outra
tupla = 1, 2, 3
print(tupla)
nova = tupla # na tupla não temos problema de shallow copy.
print(nova)
print(tupla)
outra = 4, 5, 6
nova = nova + outra
print(nova)


"""

tupla = 1, 2, 3
print(dir(tupla))