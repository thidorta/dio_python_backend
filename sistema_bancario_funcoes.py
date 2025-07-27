import time

def verificar_cpf(cpf, usuarios):
    for usuario in usuarios:
        usuario_existe = usuario.get("cpf", )
        if usuario_existe == cpf:
            return usuario_existe
    return False
    
def cria_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = verificar_cpf(cpf, usuarios) # verifica que não tem nenhum cpf igual

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/siglaEF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("==== Usuário criado com sucesso! ====")

def cria_conta(agencia, usuarios, contas, numero_conta):
    cpf = input("Informe o CPF: ")
    usuario = verificar_cpf(cpf, usuarios) 
    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    else:
        print("\n@@@ Não existe usuário cadastrado com esse CPF! @@@")
        return
    print("==== Conta-corrente criada com sucesso! ====")

def listar_usuarios(usuarios):
    lista_usuarios = list()
    for usuario in usuarios:
        print(usuario)

def menu():
    print(
    """
    ============== Sistema Bancário ==============

        1. Depositar
        2. Sacar
        3. Extrato
        4. Cadastrar usuário
        5. Cadastrar conta
        6. Listar usuários
        7. Sair

    =========== Digite a opção desejada! ==========
    """
    )

def exit():
    print(
    """
    =========== Obrigado por utilizar nosso sistema! ===========
    """
    )

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (valor <= saldo) and (valor <= limite) and (numero_saques < limite_saques) and (valor > 0):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1   
            print(f"Saque de R${valor} efetuado com sucesso!") 
    else:
        print("Não é possível efetual o saque!")     
    return saldo, extrato, numero_saques

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"    
        print(f"Depósito de R${valor} efetuado com sucesso!") 
    else:
        print("Não é possível efetual o depósito!")  
    return saldo, extrato

def mostrar_extrato(saldo, extrato):
    print("\n######### Extrato #########")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("############################\n")

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = list()
    contas = list()
    numero_conta = 0

    while True:

        menu()

        opcao = int(input())

        if opcao == 1:
            valor = int(input("Informe o valor desejado de depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            time.sleep(2)

        elif opcao == 2:
            valor = int(input("Informe o valor desejado de saque: "))
            saldo, extrato, numero_saques = saque(
                saldo, 
                valor, 
                extrato, 
                limite, 
                numero_saques, 
                LIMITE_SAQUES
            )
            time.sleep(2)

        elif opcao == 3:
            mostrar_extrato(saldo, extrato)
            time.sleep(2)

        elif opcao == 4:
            cria_usuario(usuarios)
            time.sleep(2)

        elif opcao == 5:
            numero_conta += 1
            cria_conta(AGENCIA, usuarios, contas, numero_conta)
            time.sleep(2)

        elif opcao == 7:
            exit()
            break
        
        elif opcao == 6:
            listar_usuarios(usuarios)
            time.sleep(2)
            
        else:
            print("Opção incorreta. Por favor, digite a opção desejada novamente!")
            time.sleep(1)
main()