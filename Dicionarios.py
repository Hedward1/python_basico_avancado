"""
        DICIONARIOS

OBS: EM ALGUMAS LINGUAGENS DE PROGRAMAÇÃO SÃO CONHECIDOS POR MAPAS

DICIONÁRIOS SÃO COLEÇÕES DO TIPO CHAVE/VALOR
DICIONARIOS SÃO REPRESENTADOSPOR CHAVES {}

print(type({}))

OBS:
OBS TANTO CHAVE QUANTO VALOR PODEM SER
    - Chave e valor são separadas por 2 pontos 'chave:valor'
    - Tanto chave quanto valor podem ser de qualquer tipo dedado;
    - Podemos misturar tipos de dados;

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'Py': 'Paraguai'}
print(paises)
print(type(paises))
# Forma 2
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que  lista/tupla
print(paises['br'])
# print(paises['ru'])
# Caso tentamos fazer acesso prop uma chave que não existe, o erro se chama 'keyerror'

# Forma 2
#Acessando via GET
print(paises.get('br'))
print(paises.get('ru'))

# CASO GET NÃO ENCONTRE O ONJETO, RETORNARÁ OBJETO NONE
pais = paises.get('ru')
if pais:pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')
    print(f'Encontrei o pais {pais}')
else:
    print('não encontrei o pais')

# PODEMOS DEFINIR UM VALOR PADRÃO PARA CASO NÃO ENCONTREMOS O OBJETO COM A CHAVE PEDIDA

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o pais {pais}')

# podemos verificar se determinada chave se encontra em um dicionario
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises
    russia = paises['ru']

# podemos utilizar qualquer tipo de dado (int, float.... lista, tupla dicionario, como chaves de dicionarios)

localidades = {
    (35.6895, 39.6917): 'Escritorio em Tókio',
    (40.7128, 74.0060): 'Escritorio em Nova York',
    (37.7749, 122.4194): 'Escritorio em São Paulo',
}

print(localidades)
print(type(localidades))

#adicionar elementos
receita = {'jan': 100, 'fev': 120, 'mar': 300}

#forma 1 MAIS COMUM
receita['abr'] = 350
print(receita)

# forma 2
novo_dado = {'mai': 500}  # receita.update({'mai': 500})
receita.update(novo_dado)
print(receita)
# Atualizando dados em um dicionario
# FORMA 1
receita['mai']= 550
print(receita)
# FORMA 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A FORMA DE ADICIONAR OU ATULIZAR DADOS EM UM DICIONARIO É A MESMA.
# CONCLUSÃO 2: EM DICIONARIOS NÃO PODEMOS TER CHAVES REPETIDAS.


# REMOVER DADOS DE UM DICIONÁRIO

# FORMA 1
receita = {'jan': 100, 'fev': 120, 'mar': 300}
ret = receita.pop('mar')
print(receita)
print(ret)
# FORMA 2
del receita['fev']
print(receita)
# SE NÃO EXISTIR A CHAVE, KEYERROR SERÁ GERADO
# NESTE CASO O VALOR REMOVIDO NÃO SERÁ RETORNADO.

# IMAGINE QUE TEM UM COMERCIO ELETRÔNICO, ONDE TEMOS UM CARRINHOS DE COMPRAS NO QUAL ADICIONAMOS PRODUTOS

carrinho = []
produto1 = ['playstation4', 1, 2300.00]
produto2 = ['God of war 4', 1, 150.00]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# teriamos que saber o indice de cada informação do produto

# 2 - Poderiamos utilizar uma Tupla para isso ? sim

produto1 = ('playstation4', 1, 2300.00)
produto2 = ('God of war 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

# teriamos que saber o indice de cada informação do produto

# 3 poderiamos utilizar um dicionário para isso ?

carrinho = []
produto1 = {'nome': 'Playstation4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of war4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# desta forma facilmente adicionamos ou removemos produtos do carrinho e em cada produto podemos ter a certesa
# de cada informação

# zerar dados
d.clear()

print(d)


d = dict(a=1, b=2, c=3)

print(dict(d))
print(type(d))

"""

# forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe 2 parametros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atriibuir a essa o chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 10), 'novo')
print(veja)