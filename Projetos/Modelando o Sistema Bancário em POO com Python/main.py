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

# Esboço da UML implementado!!!

# Na pasta "Classes" estão as classes, com seus respectivos atributos e métodos

# Aqui é o corpo principal da aplicação bancária. No momento, há apenas a função exibir menu.
# AGORA falta implementar a aplicação