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
[0] - Sair""")
    
    print("".center(50,"="))

def deposito():
    """
    Realiza um depósito na conta bancária.

    Saída:
    None
    """

    global saldo # Saldo é um valor global, que vem de fora!
    print("DEPOSITO ".center(50," "))

    valor_depositado = float(input("\nDigite o valor a ser depositado: R$"))

    if valor_depositado > 0:
        saldo += valor_depositado
        lista_extrato.append(valor_depositado)
    else:
        print("\n !!! Insira o valor válido para ser depositado (>0) !!!\n")

def saque():
    """
    Realiza um saque na conta bancária, considerando as restrições de limite e saldo disponível.

    Saída:
    None
    """

    global saldo, qtd_saque_diario # Saldo e qtd_s_d é um valor global, que vem de fora!
    print("SAQUE".center(50," "))
    
    valor_sacado = float(input("\nDigite o valor a ser sacado: R$"))

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
   
def extrato():
    """
    Exibe o extrato da conta bancária, mostrando as transações de depósitos e saques.

    Saída:
    None
    """
    
    for item in lista_extrato:
        if item<0: # Saque
            print(f"\033[0;31mC: R${abs(item):.2f}\033[0m")
        else: # Deposito
            print(f"\033[0;32mD: R${item:.2f}\033[0m")



################################################################

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
        deposito()
    elif opcao == 2:
        saque()
    elif opcao == 3:
        extrato()
    elif opcao == 0:
        break 
    else:
        print("ERRO!!! Opção inválida.\nTente novamente\n")
        continue
    
    #print(f"\nSALDO: R${saldo:.2f}")



