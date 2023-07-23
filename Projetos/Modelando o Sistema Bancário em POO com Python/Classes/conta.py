from deposito import *
from saque import *


class Conta():
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        return self._saldo
    
    def nova_conta(self, cliente, numero):

        # Definir

        pass

    def sacar(self, valor):
        saque = Saque(valor)


        pass

    def depositar(self, valor):
        deposito = Deposito(valor)
        self._saldo = deposito.registrar(self)
    

