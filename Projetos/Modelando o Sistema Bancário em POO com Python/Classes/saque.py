from transacao import *

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):

        if self._valor <= 0: # Se valor for menor que 0
            print("\n !!! Insira um valor para saque válido !!! \n")
        else:
            if qtd_saque_diario>=3: # Se ultrapassou a limite qtd
                print(f"\nERRO!!! Quantidade de saque diário ultrapassou o limite de {conta._limite_saques} vez(es) ao dia.\n")
            elif self._valor>500: # Se ultrapassou o limite saque
                print(f"\nERRO!!! Valor de saque ultrapassou o limite máximo diário de R${conta._limite_valor:.2f}\n")
            elif self._valor>conta._saldo: # Se valor for maior que o conta._saldo
                print("\nERRO!!! Valor a ser sacado maior que o conta._saldo.")
                print(f"Valor a ser sacado: R${self._valor:.2f}.")
                print(f"conta._saldo: R${conta._saldo:.2f}.\n")
            else: # Caso ocorra tudo certo
                conta._saldo -= self._valor
                qtd_saque_diario += 1
                conta._historico.adicionar_transacao(self)
    
        return conta._saldo