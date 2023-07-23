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

    @classmethod
    def criar_cliente(cls):
        # CPF
        CPF = input("Digite o CPF do novo usuário: ")
        # Nome
        nome = input("Digite o nome do novo usuário: ")
        # Data de Nascimento
        data_nasc = input("Digite a data de nascimento do novo usuário(FORMATO: dd/mm/aaaa): ")
        # Endereço
        endereco = input("Digite o endereço do novo usuário (FORMATO: logradouro,nro-bairro-cidade/siglaEstado): ")

        return cls(endereco, CPF, nome, data_nasc)
    