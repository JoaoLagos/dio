from Classes.cliente import Cliente

class PessoaFisica(Cliente):

    def __init__(self, endereco, CPF, nome, data_nasc):
        super().__init__(endereco)
        self._CPF = CPF
        self._nome = nome
        self._data_nascimento = data_nasc

    @property
    def CPF(self):
        return self._CPF
    @property
    def nome(self):
        return self._nome
    @property
    def data_nascimento(self):
        return self._data_nascimento
    