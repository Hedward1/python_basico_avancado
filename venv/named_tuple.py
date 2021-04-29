"""

NAME TUPLE -> SÃO TUPLA, DIFERENCIADAS, ONDE, ESPECIFICAMOS UM NOME PARA A MESMA E TAMBEM PARÂMETROS

"""
from collections import deque

#  precisamos definir o nome e parâmetros

#  forma 1
#cachorro = collections.namedtuple('cachorro', 'idade raca nome')

#  forma 2
#cachorro = collections.namedtuple('cachorro', 'idade, raca, nome')

#  forma 3
cachorro = collections.namedtuple('cachorro', ['idade', 'raca', 'nome'])
ray = cachorro(idade=2, raca='Pastor Alemão', nome='Ray')

print(ray)
