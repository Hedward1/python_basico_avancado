"""
PODE SER FEITA DE DUAS MANEIRAS:
    1 - MULTIDERIVAÇÃO DIRETA.
    2 - MULTIDERIVAÇÃO INDIRETA.



class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# exemplo indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimenta(self):
        return f'eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'O animal {self._Animal__nome} está nadando.'

    def cumprimenta(self):
        return f'Eu sou {self._Animal__nome} do mar.'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'O animal {self._Animal__nome} está correndo'

    def cumprimenta(self):
        return f'Eu sou {self._Animal__nome} da terra.'


class Pinguim(Terrestre, Aquatico): # se inverter as heranças ele irá utilizar o metodo cumprimenta da primeira casa
    def __init__(self, nome):
        super().__init__(nome)

# testando

baleia = Aquatico('wally')
print(baleia.nadar())
print(baleia.cumprimenta())

tatu = Terrestre('bola')
print(tatu.andar())
print(tatu.cumprimenta())

linux = Pinguim('linux')
print(linux.andar())
print(linux.nadar())
print(linux.cumprimenta())  # Eu sou linux da terra. #### Method resolution order na prox aula
                            # MRO - é a sequênci das heranças, podendo ser usado com o help()

print(f'O linux é instancia de Pinguim ? {isinstance(linux,Pinguim)}')
print(f'O linux é instancia de Aquatico ? {isinstance(linux,Aquatico)}')
print(f'O linux é instancia de Terrestre ? {isinstance(linux,Terrestre)}')
print(f'O linux é instancia de Animal ? {isinstance(linux,Animal)}')
print(f'O linux é instancia de object ? {isinstance(linux,object)}')

print(Pinguim.__mro__)
print(Pinguim.mro())

