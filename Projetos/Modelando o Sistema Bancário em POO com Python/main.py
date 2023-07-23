#TODO: Fiz a OPÇÃO 1, OPÇÃO 4 e OPÇÃO 5, falta fazer as demais. 
#TODO: Tirar o criar_cliente de cliente.py e passar para o main.py

from Classes.pessoa_fisica import *
from Classes.conta_corrente import *

def exibeMenu():
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

def busca_CPF(lista, CPF):
    for i in range(len(lista)):
            if CPF == lista[i].CPF:
                return lista[i]

lista_clientes = []

while True:
    exibeMenu()
    opcao = int(input("Digite a opção desejada: "))
    print("".center(50,"="))
    print("")

    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        CPF = input("Digite o CPF: ")
        cliente = busca_CPF(lista_clientes, CPF)
        if not cliente:
            lista_clientes.append(PessoaFisica.criar_cliente(CPF))
            print(lista_clientes)
        else:
            print("CPF já cadastrado!")
    elif opcao == 5:
        print("CRIANDO CONTA CORRENTE:")

        # Busca de CPF
        CPF = input("Digite o CPF do usuário que deseja criar uma conta corrente: ")
        cliente = busca_CPF(lista_clientes, CPF)
        if cliente:
            conta_nova = ContaCorrente.criar_conta_corrente(cliente)
            cliente.adicionar_conta(conta_nova)
            print(cliente.contas)
        else:
            print("Não é possivel criar uma conta corrente. CPF inexistente!")
    elif opcao == 6:
        pass
    elif opcao == 7:
        pass
    elif opcao == 0:
        break
    else:
        print("ERRO!!! Opção inválida.\nTente novamente\n")
        continue
    