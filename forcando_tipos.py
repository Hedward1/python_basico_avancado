"""
Forçando tipos de dados com decoradores


"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(novo_args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*args, **kwargs)
        return converte
    return decorador


@forca_tipo
def repete_msg(msg, vezes):
    for vezes in range(vezes):
        print(msg)


