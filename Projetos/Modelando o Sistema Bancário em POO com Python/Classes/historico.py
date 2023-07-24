from Classes.deposito import *
from Classes.saque import *

class Historico():
    def __init__(self,):
        self.lista_transacao = []

    def adicionar_transacao(self, transacao):
        self.lista_transacao.append(transacao)