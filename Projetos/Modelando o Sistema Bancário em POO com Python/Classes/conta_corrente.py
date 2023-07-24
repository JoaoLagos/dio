from Classes.conta import *

class ContaCorrente(Conta):

    def __init__(self,numero, cliente, limite_valor=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite_valor = limite_valor
        self._limite_saques = limite_saques

    def sacar(self, valor):
        if valor <= 0: # Se valor for menor que 0
            print("\n !!! Insira um valor para saque válido !!! \n")
        else:
            qtd_saque_diario = 0
            for item in self.historico.lista_transacao:
                if (isinstance(item, Saque)):
                    qtd_saque_diario += 1
            if qtd_saque_diario>=3: # Se ultrapassou a limite qtd
                print(f"\nERRO!!! Quantidade de saque diário ultrapassou o limite de {self._limite_saques} vez(es) ao dia.\n")
            elif valor>500: # Se ultrapassou o limite saque
                print(f"\nERRO!!! Valor de saque ultrapassou o limite máximo diário de R${self._limite_valor:.2f}\n")
            elif valor>self.saldo: # Se valor for maior que o self._saldo
                print("\nERRO!!! Valor a ser sacado maior que o saldo.")
                print(f"Valor a ser sacado: R${valor:.2f}.")
                print(f"saldo: R${self.saldo:.2f}.\n")
            else: # Caso ocorra tudo certo
                self._saldo -= valor
                print("Saque realizado com sucesso!!!")
                return True
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!!!")
            return True
        else:
            print("\nDeposito não efetuado !!! Insira o valor válido para ser depositado (>0) !!!\n")
        return False
        



