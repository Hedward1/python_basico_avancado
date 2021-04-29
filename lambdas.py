"""
Utilizando lambdas
Conhecidas por Expressões Lambdas, funções sem nome, ou seja, anonimas

#função me python
def funcao(x):
    return 3 * x + 1


print(funcao(4))


# Expressao Lambda
lambda x: 3 * x + 1

# como utilizar lambda ?
calc = lambda x: 3 * x + 1
print(calc(4))

# podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nomes, sobrenomes: nomes.strip().tittle() + ' ' + sobrenomes.strip().tittle()

# Em funções python podemos ter nenhuma ou várias entradas
amar = lambda: 'Como não amar o python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: x * y ** 0.5
tres = lambda x, y, z : 3 / (1 / x + 1 / y + 1 / z)
# n = lambda x1, x2, ... xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# se passarmos mais argumentos que parâmetros esperados teremos TypeError
"""




