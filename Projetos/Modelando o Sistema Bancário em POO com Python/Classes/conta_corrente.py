from Classes.conta import *

class ContaCorrente(Conta):

    def __init__(self,numero, cliente, limite_valor=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite_valor = limite_valor
        self._limite_saques = limite_saques

    @classmethod
    def criar_conta_corrente(cls, cliente):
        numero = 10
        cliente = cliente

        return cls(numero, cliente, limite_valor=500, limite_saques=3)


