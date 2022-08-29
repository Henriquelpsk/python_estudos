class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        return (self.__saldo + self.__limite) >= valor

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"Saldo insuficiente: {self.__saldo}R$ | Limite:{self.limite}R$")

    def transferir(self, valor, destino):
        if (self.__pode_sacar(valor)):
            self.sacar(valor)
            destino.deposito(valor)
        else:
            print(f"Saldo insuficiente: {self.__saldo}R$ | Limite:{self.__limite}R$")

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é de {self.__saldo}R$")

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite



