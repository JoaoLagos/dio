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
    cliente = busca_CPF(lista_clientes, CPF)

    if not cliente: # Se CPF não exister no banco de dados
        # Nome
        nome = input("Digite o nome do novo usuário: ")
        # Data de Nascimento
        data_nasc = input("Digite a data de nascimento do novo usuário(FORMATO: dd/mm/aaaa): ")
        # Endereço
        endereco = input("Digite o endereço do novo usuário (FORMATO: logradouro,nro-bairro-cidade/siglaEstado): ")

        return PessoaFisica(endereco, CPF, nome, data_nasc)

def busca_CPF(lista, CPF):
    for i in range(len(lista)):
            if CPF == lista[i].CPF:
                return lista[i]

def visualizar_contas(lista):
    print("".center(50,"="))
    print("CONTAS CORRENTES".center(50," "))
    for conta in lista:
        print("Titular: ", conta.cliente.nome)
        print("Agência: ", conta.agencia)
        print("Número da Conta: ", conta.numero)
        print("".center(50,"-"))
    print("".center(50,"="))
    print("\n")

def visualizar_usuarios(lista):
    print("".center(50,"="))
    print("USUÁRIOS".center(50," "))
    for usuario in lista:
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
        pass
    
    elif opcao == 2: # SACAR
        pass

    elif opcao == 3: # EXTRATO (Histórico)
        pass

    elif opcao == 4:
        novo_cliente = criar_cliente()
        lista_clientes.append(novo_cliente)
        print(lista_clientes)          
    elif opcao == 5:
        print("CRIANDO CONTA CORRENTE:")

        # Busca de CPF
        CPF = input("Digite o CPF do usuário que deseja criar uma conta corrente: ")
        cliente = busca_CPF(lista_clientes, CPF)
        if cliente:
            conta_nova = ContaCorrente.nova_conta(cliente, len(lista_contas)+1)
            cliente.adicionar_conta(conta_nova)
            lista_contas.append(conta_nova)
            print(cliente.contas)
        else:
            print("Não é possivel criar uma conta corrente. CPF inexistente!")
    elif opcao == 6:
        visualizar_contas(lista_contas)
    elif opcao == 7:
        visualizar_usuarios(lista_clientes)
    elif opcao == 0:
        break
    else:
        print("ERRO!!! Opção inválida.\nTente novamente\n")
        continue
    