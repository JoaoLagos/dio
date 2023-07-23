from cliente import *

class PessoaFisica(Cliente):

    def __init__(self, CPF, nome, data_nasc):
        self.CPF = CPF
        self.nome = nome
        self.data_nascimento = data_nasc