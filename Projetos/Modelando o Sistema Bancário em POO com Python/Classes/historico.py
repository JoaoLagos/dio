from deposito import *
from saque import *

class Historico():
    def __init__(self,):
        self.lista_transacao = []

    def adicionar_transacao(self, transacao):
        
        if isinstance(transacao, Deposito):
            self.lista_transacao.append(transacao._valor)
        elif isinstance(transacao, Saque):
            self.lista_transacao.append(-transacao._valor)