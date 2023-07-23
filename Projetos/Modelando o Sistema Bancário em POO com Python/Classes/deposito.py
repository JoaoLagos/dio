from transacao import *

class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):

        if self._valor > 0:
            conta._saldo += self._valor
            conta._historico.adicionar_transacao(self)
        else:
            print("\n !!! Insira o valor válido para ser depositado (>0) !!!\n")

        return conta._saldo