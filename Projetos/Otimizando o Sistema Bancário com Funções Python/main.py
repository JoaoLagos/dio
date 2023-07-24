def exibeMenu():
    """
    Exibe o menu bancário com opções disponíveis e o saldo atual.

    Saída:
    None
    """
    
    print ("".center(50,"="))
    print(" MENU BANCÁRIO ".center(50," "))
    print ("".center(50,"="))

    print(f"\033[0;33mSALDO: R${saldo:.2f}\n\033[0m")

    print("""[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar novo Cliente
[5] - Criar Conta Corrente
[6] - Visualizar Contas
[7] - Visualizar Usuários
[0] - Sair""")
    
    print("".center(50,"="))

def criarUsuario(dic_usuarios):
    """
    Cria um novo usuário no sistema bancário e armazena as informações no dicionário de usuários.

    Parâmetros:
        dic_usuarios (dict): Dicionário contendo os usuários cadastrados, com CPF como chave e informações do usuário como valor.

    Saída:
        None
    """

    print("CRIANDO USUÁRIO:")

    # CPF
    CPF = input("Digite o CPF do novo usuário: ")
    if CPF not in dic_usuarios:
        # Nome
        nome = input("Digite o nome do novo usuário: ")
        # Data de Nascimento
        data_nasc = input("Digite a data de nascimento do novo usuário(FORMATO: dd/mm/aaaa): ")
        # Endereço
        endereco = input("Digite o endereço do novo usuário (FORMATO: logradouro,nro-bairro-cidade/siglaEstado): ")

        #Cria um dicionário com as informações do usuário
        dic_usuario = {
            "Nome": nome,
            "Data de Nascimento": data_nasc,
            "CPF": CPF,
            "Endereço": endereco,
            "Contas": []
        }
        #Insere o dicionario do usuário ao dicionário dos USUÁRIO"S"
        dic_usuarios[CPF] = dic_usuario

        print("\n*** USUÁRIO CRIADO COM SUCESSO ***\n")
    else:
        print("\nERRO!\nJá existe usuário com esse CPF.\n")
    
def criarContaCorrente(dic_usuarios, lista_contas_correntes):
    """
    Cria uma conta corrente associada a um usuário, se o CPF do usuário existir no banco de dados.

    Parâmetros:
        dic_usuarios (dict): Dicionário contendo os usuários cadastrados, com CPF como chave.
        lista_contas_correntes (list): Lista para armazenar as contas correntes criadas.

    Saída:
        None
    """

    print("CRIANDO CONTA CORRENTE:")

    # Busca de CPF
    CPF = input("Digite o CPF do usuário que deseja criar uma conta corrente: ")
    # Inserção, caso exista
    if CPF in dic_usuarios:
        qtd_contas = len(lista_contas_correntes)

        dic_conta_corrente = {
            "Agência": "0001",
            "Número da Conta": qtd_contas+1,
            "CPF": CPF
        }

        dic_usuarios[CPF]["Contas"].append(dic_conta_corrente["Número da Conta"])

        lista_contas_correntes.append(dic_conta_corrente)

        print("\n*** CONTA CORRENTE CRIADA COM SUCESSO ***\n")
    # Caso não exista o CPF no banco de dados dict
    else:
        print("\nERRO!!!\nUsuário Inexistente!\n")

def deposito(valor_depositado, saldo, lista_extrato,/):
    """
    Realiza um depósito na conta bancária.

    Parâmetros:
        valor_depositado (float): Valor a ser depositado na conta.
        saldo (float): Saldo atual da conta.
        lista_extrato (list): Lista para registrar as operações de depósito.

    Saída:
        None
    """

    if valor_depositado > 0:
        saldo += valor_depositado
        lista_extrato.append(valor_depositado)
    else:
        print("\n !!! Insira o valor válido para ser depositado (>0) !!!\n")

    return saldo

def saque(*,valor_sacado, saldo, lista_extrato, qtd_saque_diario, qtd_saque_diario_max, limite_saque):
    """
    Realiza um saque na conta bancária, considerando as restrições de limite e saldo disponível.

    Parâmetros:
        valor_sacado (float): Valor a ser sacado da conta.
        saldo (float): Saldo atual da conta.
        lista_extrato (list): Lista para registrar as operações de saque.
        qtd_saque_diario (int): Quantidade de saques realizados no dia.
        qtd_saque_diario_max (int): Limite máximo de saques permitidos por dia.
        limite_saque (float): Limite máximo diário para o valor de saque.

    Saída:
        float: Novo saldo após o saque ou o saldo atual caso o saque não seja realizado.
    """

    if valor_sacado <= 0: # Se valor for menor que 0
        print("\n !!! Insira um valor para saque válido !!! \n")
    else:
        if qtd_saque_diario>=3: # Se ultrapassou a limite qtd
            print(f"\nERRO!!! Quantidade de saque diário ultrapassou o limite de {qtd_saque_diario_max} vez(es) ao dia.\n")
        elif valor_sacado>500: # Se ultrapassou o limite saque
            print(f"\nERRO!!! Valor de saque ultrapassou o limite máximo diário de R${limite_saque:.2f}\n")
        elif valor_sacado>saldo: # Se valor for maior que o saldo
            print("\nERRO!!! Valor a ser sacado maior que o saldo.")
            print(f"Valor a ser sacado: R${valor_sacado:.2f}.")
            print(f"Saldo: R${saldo:.2f}.\n")
        else: # Caso ocorra tudo certo
            saldo -= valor_sacado
            qtd_saque_diario += 1
            lista_extrato.append(-valor_sacado)
    
    return saldo
   
def extrato(saldo,/,*,lista_extrato):
    """
    Exibe o extrato da conta bancária, mostrando as transações de depósitos e saques.

    Parâmetros:
        saldo (float): Saldo atual da conta bancária.
        lista_extrato (list): Lista contendo as transações de depósitos e saques.

    Saída:
        None
    """

    print("EXTRATO".center(50," "))
    print("")
    
    if len(lista_extrato)==0:
        print("\nNão houve movimentações em sua conta bancária.\n")

    for item in lista_extrato:
        if item<0: # Saque
            print(f"\033[0;31mC: R${abs(item):.2f}\033[0m")
        else: # Deposito
            print(f"\033[0;32mD: R${item:.2f}\033[0m")
    print("".center(50,"-"))
    print(f"\033[0;33mSALDO: R${saldo:.2f}\n\033[0m")

def visualizarContas(lista_contas_correntes):
    print("".center(50,"="))
    print("CONTAS CORRENTES".center(50," "))
    for conta in lista_contas_correntes:
        print("Titular: ", conta["CPF"])
        print("Agência: ", conta["Agência"])
        print("Número da Conta: ", conta["Número da Conta"])
        print("".center(50,"-"))
    print("".center(50,"="))
    print("\n")

def visualizarUsuarios(dic_usuarios):
    print("".center(50,"="))
    print("USUÁRIOS".center(50," "))
    for chave in dic_usuarios:
        print(("Nome: " + dic_usuarios[chave]["Nome"]).center(50," "))
        print("\nCPF: ", dic_usuarios[chave]["CPF"])
        print("Data de Nascimento: ", dic_usuarios[chave]["Data de Nascimento"])
        print("Endereço: ", dic_usuarios[chave]["Endereço"])
        #print("Contas: ", dic_usuarios[chave]["Contas"])
        print("Contas: ")
        for conta in dic_usuarios[chave]["Contas"]:
            print("\t", conta)
        print("".center(50,"-"))
    print("".center(50,"="))
    print("\n")

################################################################
dic_usuarios = {}
lista_contas_correntes = []

saldo = 0
qtd_saque_diario = 0
qtd_saque_diario_max = 3
limite_saque = 500
lista_extrato = []

while True:
    exibeMenu()
    opcao = int(input("Digite a opção desejada: "))
    print("".center(50,"="))
    print("")

    if opcao == 1:
        print("DEPOSITO ".center(50," "))

        valor_depositado = float(input("\nDigite o valor a ser depositado: R$"))
        saldo = deposito(valor_depositado, saldo, lista_extrato)
    elif opcao == 2:
        print("SAQUE".center(50," "))
    
        valor_sacado = float(input("\nDigite o valor a ser sacado: R$"))
        saldo = saque(
            valor_sacado=valor_sacado,
            saldo=saldo,
            lista_extrato=lista_extrato,
            qtd_saque_diario=qtd_saque_diario,
            qtd_saque_diario_max=qtd_saque_diario_max,
            limite_saque=limite_saque)
    elif opcao == 3:
        extrato(saldo, lista_extrato=lista_extrato)
    elif opcao == 4:
        criarUsuario(dic_usuarios)
        print(dic_usuarios)
    elif opcao == 5:
        criarContaCorrente(dic_usuarios, lista_contas_correntes)
        print(lista_contas_correntes)
    elif opcao == 6:
        visualizarContas(lista_contas_correntes)
    elif opcao == 7:
        visualizarUsuarios(dic_usuarios)
    elif opcao == 0:
        break 
    else:
        print("ERRO!!! Opção inválida.\nTente novamente\n")
        continue
    
    #print(f"\nSALDO: R${saldo:.2f}")

# COMENTÁRIOS:

# - criarUsuario é feito com base em DICIONÁRIO (dic_usuarios), pois posso ter acesso rápido aos dados usando chaves e não possui ordem definida, como no caso de listas para contas correntes. Também pelo fato de DICIONÁRIO ser chave:valor, pois com isso eu posso buscar o usuário através da chave (CPF). Se fosse em lista, eu teria que percorrer toda a lista até achar o elemento que tivesse aquele CPF

# - criarContaCorrente é feito com base em LISTAS (lista_contas_correntes), pois há uma ordem definida (primeira conta (1), segunda conta (2), ...), facilitando a busca pelo indice.

