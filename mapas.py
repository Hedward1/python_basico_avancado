"""
    MAPAS -> CONHECIDOS EM PYTHON COMO DICIONÁRIOS

    DICIONÁRIOS EM PYTHON SÃO REPRESENTADOR POR {}

# Iterar sobre dicionários
print(receita)

for chave in receita:
    print(chave)


for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} Recebi R$ {receita[chave]}')

# acessando as chaves
print(receita.keys())
for chave in receita.keys():
    print(receita)

# acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

#desempacotamento de dicionários
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais.
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

