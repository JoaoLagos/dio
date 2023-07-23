from conta import *

class ContaCorrente(Conta):

    def __init__(self, saldo, numero, agencia, cliente, historico, limite_valor, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite_valor = limite_valor
        self._limite_saques = limite_saques


