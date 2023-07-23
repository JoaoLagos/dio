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
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @abstractmethod # Pois cada tipo de conta (conta corrente, conta poupança) vai ter seus critérios para saque
    def sacar(self, valor):
        pass

    @abstractmethod # Pois cada tipo de conta (conta corrente, conta poupança) vai ter seus critérios para deposito
    def depositar(self, valor):
        pass
    

