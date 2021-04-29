"""
    CONJUNTOS
    - CONJUNTOS EM QUALQUER LINGUAGEM DE PROGRAMAÇÃO, ESTAMOS AFZENDO REFERÊNCIA A TEORIA DOS CONJUNTOS DA MATEMÁTICA

    - AQUI EM PYTHON SÃO CHAMADOS DE SETS

DITO ISTO, DA MESMA FORMA QUE NA MATEMÁTICA:
- SETS NÃO POSSUEM VALORES DUPLICADOS
- SETS NÃO POSSUEM VALORES ORDENADOS
- ELEMENTOS NÃO SÃO ACESSADOS VIA INDICE, CONJUNTOS NÃO SÃO INDEXADOS

CONJUNTOS SÃO BONS PARA SE UTILIZAR QUANDO PRECISAMOS ARMZENAR OS ELEMENTOS MAS NÃO NOS
IMPORTAMOS COM A ORDENAÇÃO DELES. QUANDO NÃO PRECISAMOS SE PREOCUPAR COM CHAVES, VALORES E ITENS DUPLICADOS.

OS CONJUNTOS (SETS) SÃO REFERÊNCIADOS EM PYTHON COM CHAVES {}

DIFERENÇA ENTRE CONJUNTOS E MAPAS (SETS E DICIONÁRIOS) EM PYTHON:
    - UM DICIONÁRIO TEM CHAVE/VALOR;
    - UM CONJUNTO TEM APENAS VALOR;

# DEFININDO UM CONJUNTO
# FORMA 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})# repare que temos valores repetidos.

print(s)
print(type(s))

# ao criar um conjunto, caso seja criado um valor já existente, o mesmo será ignorado sem gerar erros
# e não fará parte do conjunto

# forma 2 (mais comum)
s = set({1, 2, 3, 4, 5, 6, 7,})
print(s)
print(type(s))

if 13 in s:
    print(f'tem o 3')
else:
    print(f'não tem o 3')

# importante lembrar que alem de não termos valores duplicados, não temos ordem.
# listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print(f'lista {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 99, 2, 34, 23, 12, 1, 44, 5, 2, 34
print(f'tupla {tupla} com {len(tupla)} elementos')
# dicionarios aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')
print(f'dicionario {dicionario} com {len(dicionario)} elementos')

# conjuntos aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print(f'conjunto {conjunto} com {len(conjunto)} elementos')

# assim como todo outro conjunto pyhton, podemos colocar todos os tipos de dados misturados em Sets
s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# podemos iterar em um set normalmente
for valor in s:
    print(valor)

# usos interessantes com SETS
# imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes
# informam manualmente a cidade de onde vieram.

# nós adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos elementos
# e não ter repetição
cidades = ['BELO HORIZONTE', 'SÃO PAULO', 'CAMPO GRANDE', 'CAIUA', 'CAMPO GRANDE', 'SÃO PAULO', 'CAIUA']
print(cidades)
print(len(cidades))

print(len(set(cidades)))


# adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4) # duplicidade não gera erro e será desconsiderado
print(s)

# demover elementos
# forma 1
s.remove(3)  # não é indice, mas sim valor, como nas regras
print(s)
# obs caso não seja encontrado será gerado o erro KeyError. NENHUM VALOR É RETORNADO

#forma 2
s.discard(2)
s.discard(22) # SE O VALOR NÃO FOR ENCNONTRADO NENHUM ERRRO É GERADO
print(s)

# copiando um conjuto para outro
s = {1, 2, 3}
print(s)
# forma 1
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

# forma 2

new = s
new.add(5)
print(new)
print(s)

# PODEMOS REMOVER TODOS OS ITENS DE UM CONJUNTO
s = {1, 2, 3}
print(s)
s.clear()
print(s)

# conjuntos com nomes de estudantes únicos

# metodos matemáticos de ocnjuntos
estudantes_python = {'marcos', 'patricia', 'ellen', 'pedro', 'julia', 'guilherme'}
estudantes_java = {'fernando', 'gustavo', 'julia', 'ana', 'patricia'}

# forma1
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)
print(len(unicos1))

#forma 2 - utilizando o caractere '|'

unicos2 = estudantes_java | estudantes_python
print(unicos2)

# conjunto de estudante em ambos os cursos
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# forma 2
ambos2 = estudantes_java & estudantes_python
print(ambos2)

# estudantes que estão exclusivamente em 1 curso

exclusivos1 = estudantes_java.difference(estudantes_python)
exclusivos2 = estudantes_python.difference(estudantes_java)
print(exclusivos1)
print(exclusivos2)

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Cuiabá']
print(cidades)
print(len(cidades))
# set remove duplicidades
print(len(set(cidades)))



s.add(4)
s.add(4)  # cuplicidade é ignorado
print(s)


s.remove(3)  # conjuntos não tem indeces
            # se valor não enconytrado gera keyerror
print(s)

s.discard(22)  # se o valor nao for encontrado nenhum erro e gerado
print(s)

"""

s = {1, 2, 3}




