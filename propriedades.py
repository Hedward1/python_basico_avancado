class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f' Cliente: {self.__titular} \n Saldo: {self.__saldo}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite


conta1 = Conta(titular='Hedward', saldo=3000, limite=5000)
conta2 = Conta(titular='Deborah', saldo=3000, limite=5000)

print(conta1.extrato())
print(conta2.extrato())

soma = conta1.saldo + conta2.saldo

print(f'A soma das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 99999

print(conta1.__dict__)

print(conta1.valor_total)
print(conta2.valor_total)
