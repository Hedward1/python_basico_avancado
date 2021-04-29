"""
    DEFININDO FUNÇÕES

    - FUNÇÕES SÃO PEQUENAS PARTES DE CÓDIGO QUE REALIZAM TAREFAS ESPECÍFICAS;
    - PODEM OU NÃO REEBER ENTRADAS DE CÓDITO E RETORNAR UMA SAÍDA DE DADOS;
    - MUITO UTEIS PARA EXECUTAR ROCEDIMENTOS SIMILARES POR REPETIDAS VEZES;

    OBS: SE ESCREVER UMA FUNÇÃO QUE REALIZA VARIAS TAREFAS, FAZER UM VERIFICAÇÃO PARA QUE A FUNÇÃO SEJA SIMPLIFICADA


    JÁ URILIZAMOS VÁRIAS FUNÇÕES:
        PRINT(), LEN(), MAX(), MIN(), COUNT()...

"""

#EXEMPLO DE UTILIZAÇÃO DE FUNÇÕES:

# cores = ['azul', 'vermelho', 'amarelo', 'branco']
#
# # função integrada (built-in) do python print()
#
# print(cores)
# cores.append('roxo')
# print(cores)

"""
 em python a forma geral de definir uma função é:

def nome_da_funcao(parametros_da_funcao):
    bloco_da_entrada


onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome completo, separado por underline (Snake Case);
parametros_de_entrada -> Opicionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opicionais ou não;
bloco_da_função -> tambem chamado de corpo da função ou implementação, é onde o processamento da função acontece,
neste bloco pode ou não dar retorno da função.

OBS: VEJA QUE PARA DEFINIR UMA FUNÇÃO UTILIZAMOS A PALAVRA RESERVADA 'def', informando ao python que estamos 
definindo uma função. Tambem abrimos o blco de código com o já conhecido dois pontos ':' que é utilizado em python para 
definir blocos
"""
# definindo a primeira função


def diz_oi():
    print('Oi')

"""
OBS:
    - VEJA QUE DENTRO DAS NOSSA FUNÇÕES PODEMOS UTILIZAR OUTRAS FUNÇÕES;
    - VEJA QUE ESSA FUNÇÃO SÓ EXECUTA UMA TAREFA.
    - VEJA QUE ESSA FUNÇÃO NÃO RECEBE NENHUM PARAMETRO
    - VEJA QUE ESSA FUNÇÃO NÃO RETORNA NADA

"""
#UTILIZANDO FUNÇÕES
#chamada de execução
#diz_oi()

"""
    NUNCA ESQUECER DE EXECUTAR UMA FUNÇÃO COM OS ()
"""


def cantar_parabens():
    print('parabens pra voce')
    print('nesta data querida')
    print('... viva o aniversariante')

# cantar_parabens()
#
# for n in range(5):
#     print(n)
#     cantar_parabens()


canta = cantar_parabens

