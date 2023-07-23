from Classes.transacao import *

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        saldo = conta.saldo

        if self.valor <= 0: # Se valor for menor que 0
            print("\n !!! Insira um valor para saque válido !!! \n")
        else:
            if qtd_saque_diario>=3: # Se ultrapassou a limite qtd
                print(f"\nERRO!!! Quantidade de saque diário ultrapassou o limite de {conta._limite_saques} vez(es) ao dia.\n")
            elif self.valor>500: # Se ultrapassou o limite saque
                print(f"\nERRO!!! Valor de saque ultrapassou o limite máximo diário de R${conta._limite_valor:.2f}\n")
            elif self.valor>conta.saldo: # Se valor for maior que o conta._saldo
                print("\nERRO!!! Valor a ser sacado maior que o conta._saldo.")
                print(f"Valor a ser sacado: R${self.valor:.2f}.")
                print(f"conta._saldo: R${conta.saldo:.2f}.\n")
            else: # Caso ocorra tudo certo
                saldo -= self.valor
                qtd_saque_diario += 1
                conta.historico.adicionar_transacao(self)
    
        return saldo