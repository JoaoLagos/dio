from deposito import *
from saque import *

class Cliente:

    def __init__(self, endereco=None, contas=[]):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        if conta in self._contas:
            if isinstance(transacao, Deposito):
                conta.depositar(transacao._valor)
            elif isinstance(transacao, Saque):
                conta.sacar(transacao._valor)
            else:
                print("ERRO!!!")
        else:
            print("O usuário ainda não possui uma conta!")

    def adicionar_conta(self, conta):
        print("CRIANDO CONTA CORRENTE:")
        self._contas.append(conta)
