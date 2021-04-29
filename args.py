"""
É UM PARAMETR COMO OUTRO QUALQUER. SIGNIFIFCA QUE PODERÁ SER CHAMADO, DESDE QUE COMECE COM *.
*xis.

MAS POR CONVENÇÃO, UTILIZAMOS O *ARGS PARA DEFINILO

MA SOQUE É O ARGS ?
COLOCA OS VALORES EXTRAS INFORMADOS COMO UM ENTRADA EM UMA TUPLA, SENDO AS TUPLAS IMUTÁVEIS
"""


def soma_todos_os_numeros (*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador
print(soma_todos_os_numeros(*numeros))

# OBS: O * serve para que informemos ao Python que estamos passando como argumento uma coleçao de dados.
# Desta forma, ele saberá que precisará antes desempacotar estes dados