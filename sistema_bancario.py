import time

menu = """
######### Sistema Bancário #########

    1. Depositar
    2. Sacar
    3. Extrato
    4. Sair

######### Digite a opção desejada! #########
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
exit = """

    ##### Obrigado por utilizar nosso sistema! #####
"""

while True:
    
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))
        if valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > limite:
            print("Valor do saque excede o limite permitido.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso!")
    elif opcao == "3":
        print("\n######### Extrato #########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("############################\n")
    elif opcao == "4":
        print(exit)
        break
    time.sleep(2)