from Classes.deposito import *
from Classes.saque import *

class Cliente:

    def __init__(self, endereco=None):
        self._endereco = endereco
        self._contas = []

    @property
    def endereco(self):
        return self._endereco
    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        if conta in self._contas:
            if isinstance(transacao, Deposito):
                conta.depositar(transacao.valor)
            elif isinstance(transacao, Saque):
                conta.sacar(transacao.valor)
            else:
                print("ERRO!!!")
        else:
            print("O usuário ainda não possui uma conta!")

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print("Conta corrente adicionada.")
