from Classes.deposito import *
from Classes.saque import *
from Classes.historico import *


class Conta():
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saque = Saque(valor)
        self.saldo = saque.registrar(self)

    def depositar(self, valor):
        deposito = Deposito(valor)
        self._saldo = deposito.registrar(self)
    

