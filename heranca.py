"""
Quando uma classe herda de outra classe, tanto os atributos quanto os métodos

"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # forma incomum de acessar a classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # forma comum de acessar classe.
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionario: {self.__matricula}; Nome: {self._Pessoa__nome};'


pessoa1 = Cliente('Angelina', 'Jolie', '123456789-0', 5000)
pessoa2 = Funcionario('Hedward', 'Cordeiro', '789456123-0', 8000)

print(pessoa1.nome_completo())
print(pessoa2.nome_completo())

print(pessoa1.__dict__)
print(pessoa2.__dict__)

