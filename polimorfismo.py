"""
POO - POLIMORFISMO

POLI - MUITAS
MORFISMO - FORMAS

QUANDO REENPLEMENTA UM MÉTODO NA CLASSE PAI NASS CLASSES FILHAS ESTAMOS RELIZANDO UM SOBRESCRITA DE MÉTODO.
(Overriding)

O Overriding É A SXCÊNCIA DA MLEHOR REPRESENTAÇÃO DO POLIMORFISMO
"""

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise   NotImplementedError(f'a classe filha precisa implementar este método')

    def comer(self):
        print(f'{self.__nome} está comendo ...')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau!')

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala squik! ')


felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mikey = Rato('Mikey')
mikey.comer()
mikey.falar()

