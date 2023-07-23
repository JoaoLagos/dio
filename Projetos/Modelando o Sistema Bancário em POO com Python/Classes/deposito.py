from Classes.transacao import *

class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):

        if self.valor > 0:
            saldo = conta.saldo
            saldo += self.valor
            conta.historico.adicionar_transacao(self)
        else:
            print("\n !!! Insira o valor válido para ser depositado (>0) !!!\n")

        return saldo