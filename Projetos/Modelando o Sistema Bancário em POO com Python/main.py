#TODO: Fiz a OPÇÃO (4,5,6,7), falta fazer as demais. 
#TODO: Tirar o criar_cliente de cliente.py e passar para o main.py

from Classes.pessoa_fisica import *
from Classes.conta_corrente import *

def exibe_menu():
    """
    Exibe o menu bancário com opções disponíveis e o saldo atual.

    Saída:
    None
    """
    
    print ("".center(50,"="))
    print(" MENU BANCÁRIO ".center(50," "))
    print ("".center(50,"="))

    #print(f"\033[0;33mSALDO: R${saldo:.2f}\n\033[0m")

    print("""[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar novo Cliente
[5] - Criar Conta Corrente
[6] - Visualizar Contas
[7] - Visualizar Usuários
[0] - Sair""")
    
    print("".center(50,"="))

def criar_cliente():
    print("CRIANDO CLIENTE...")
    # CPF
    CPF = input("Digite o CPF: ")
    cliente = busca_CPF(CPF)

    if not cliente: # Se CPF não exister no banco de dados
        # Nome
        nome = input("Digite o nome do novo usuário: ")
        # Data de Nascimento
        data_nasc = input("Digite a data de nascimento do novo usuário(FORMATO: dd/mm/aaaa): ")
        # Endereço
        endereco = input("Digite o endereço do novo usuário (FORMATO: logradouro,nro-bairro-cidade/siglaEstado): ")

        novo_cliente = PessoaFisica(endereco, CPF, nome, data_nasc)

        lista_clientes.append(novo_cliente)

def criar_conta_corrente():
    print("CRIANDO CONTA CORRENTE:")

    # Busca de CPF
    CPF = input("Digite o CPF do usuário que deseja criar uma conta corrente: ")
    cliente = busca_CPF(CPF)
    if cliente:
        conta_nova = ContaCorrente.nova_conta(cliente, len(lista_contas)+1)
        cliente.adicionar_conta(conta_nova)
        lista_contas.append(conta_nova)
    else:
        print("Não é possivel criar uma conta corrente. CPF inexistente!")

def depositar():
    print("DEPOSITO".center(50," "))

    num_conta = int(input("\nDigite o número da conta que deseja depositar: "))
    conta = busca_conta_por_numero(num_conta)
    if conta:
        valor = int(input("Digite o valor a ser depositado: R$"))
        deposito = Deposito(valor)
        deposito.registrar(conta)

        print(conta.saldo)
    else:
        print("Deposito não efetuado!!! Motivo: Conta inválida.")

def sacar():
    print("SAQUE".center(50," "))

    num_conta = int(input("\nDigite o número da conta que deseja sacar: "))
    conta = busca_conta_por_numero(num_conta)
    if conta:
        valor = int(input("Digite o valor a ser sacado: R$"))
        saque = Saque(valor)
        saque.registrar(conta)
    else:
        print("Deposito não efetuado!!! Motivo: Conta inválida.")

def extrato():
    print("EXTRATO".center(50," "))
    print("")

    num_conta = int(input("\nDigite o número da conta que deseja verificar o extrato: "))
    conta = busca_conta_por_numero(num_conta)
    if conta:
        if len(conta.historico.lista_transacao)==0:
            print("\nNão houve movimentações em sua conta bancária.\n")
        else:
            for item in conta.historico.lista_transacao:
                if isinstance(item, Saque): # Saque
                    print(f"\033[0;31mC: R${item.valor:.2f}\033[0m")
                elif isinstance(item, Deposito): # Deposito
                    print(f"\033[0;32mD: R${item.valor:.2f}\033[0m")
                else:
                    print("ERRO de tipo de transacao! Verificar com o banco mais próximo.")
            
            print("".center(50,"-"))
            print(f"\033[0;33mSALDO: R${conta.saldo:.2f}\n\033[0m")
    else:
        print("Conta Inexistente!!!")

def busca_conta_por_numero(num_conta):
    for conta in lista_contas:
        if conta.numero == num_conta:
            return conta

def busca_CPF(CPF):
    for i in range(len(lista_clientes)):
            if CPF == lista_clientes[i].CPF:
                return lista_clientes[i]

def visualizar_contas():
    print("".center(50,"="))
    print("CONTAS CORRENTES".center(50," "))
    for conta in lista_contas:
        print("Titular: ", conta.cliente.nome)
        print("Agência: ", conta.agencia)
        print("Número da Conta: ", conta.numero)
        print("".center(50,"-"))
    print("".center(50,"="))
    print("\n")

def visualizar_usuarios():
    print("".center(50,"="))
    print("USUÁRIOS".center(50," "))
    for usuario in lista_clientes:
        print(("Nome: " + usuario.nome).center(50," "))
        print("\nCPF: ", usuario.CPF)
        print("Data de Nascimento: ", usuario.data_nascimento)
        print("Endereço: ", usuario.endereco)
        print("Contas: ")
        for conta in usuario.contas:
            print("\t", conta.numero)
        print("".center(50,"-"))
    print("".center(50,"="))
    print("\n")

lista_clientes = []
lista_contas = []

while True:
    exibe_menu()
    opcao = int(input("Digite a opção desejada: "))
    print("".center(50,"="))
    print("")

    if opcao == 1: # DEPOSITAR     # Lembrando que, para depos, sac e extr, devemos pedir primeiro a conta no qual devemos realizar a operação. E, depois, realizar a operação nessa conta!!!
        depositar()
    
    elif opcao == 2: # SACAR
        sacar()

    elif opcao == 3: # EXTRATO (Histórico)
        extrato()

    elif opcao == 4:
        criar_cliente()
        print(lista_clientes)          
    elif opcao == 5:
        criar_conta_corrente()
        print(lista_contas)
    elif opcao == 6:
        visualizar_contas()
    elif opcao == 7:
        visualizar_usuarios()
    elif opcao == 0:
        break
    else:
        print("ERRO!!! Opção inválida.\nTente novamente\n")
        continue
    