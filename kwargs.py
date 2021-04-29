"""
**kuargs

poderiamos chamar este parametro de **xix

Diferente do *args, o **kuargs exige que utilizemos parâmetros nomeados, e transforma esses parametros extras
em um dicionário

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'{pessoa.title()} gosta da cor {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernando='azul', vanessa='branco')

# os parametros *args e *kuargs não são obrigatorios.

cores_favoritas()
cores_favoritas(hedward='roxa')

def cumprimento_especial(**kwargs):
    if 'Geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um comprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'não tenho certeza de quem voce é'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

# nas nossas funções podemos ter (NESTA ORDEM):
# - Parâmetros obrigatórios
# - *args
# - Parâmetros default (não obrigatórios)
# - **kwargs

def minha_funcao (idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome.title()} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(8, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'felipe', eu='não', voce='vai')
minha_funcao(19, 'carla', 9, 3, java=False, python=True)

# DESEMPACOTAR KWARGS
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


lista = [1, 2, 3]
tupla = 1, 2, 3
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OS NOMES DA CHAVE EM UM DICIONARIO DEVEM SER OS MESMOS DO PARÂMETROS DA FUNÇÃO
dicionario = dict(a=1, b=2, c=3, nome='geek')
soma_multiplos_numeros(** dicionario, lang='python')