from datetime import datetime


banco = {}


def criar_conta():
    numero_conta = input("Digite o número da nova conta: ")
    if numero_conta in banco:
        print("Essa conta já existe.")
    else:
        nome_cliente = input("Digite o nome do titular da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        banco[numero_conta] = {
            'nome': nome_cliente,
            'saldo': saldo_inicial,
            'saques_realizados': 0,
            'ultimo_saque': None  
        }
        print(f"Conta {numero_conta} criada com sucesso!")


def verificar_limite_saque(numero_conta):
    conta = banco[numero_conta]
    hoje = datetime.now().date()
    
    
    if conta['ultimo_saque'] != hoje:
        conta['saques_realizados'] = 0
        conta['ultimo_saque'] = hoje
    
    if conta['saques_realizados'] >= 3:
        print("Você atingiu o limite de 3 saques por dia.")
        return False
    return True


def sacar():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in banco:
        valor = float(input("Digite o valor a ser sacado (máx. R$ 500): "))
        
        if valor > 500:
            print("O valor máximo para saque é R$ 500.")
            return
        
        if not verificar_limite_saque(numero_conta):
            return
        
        if banco[numero_conta]['saldo'] >= valor:
            banco[numero_conta]['saldo'] -= valor
            banco[numero_conta]['saques_realizados'] += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Conta não encontrada.")


def depositar():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in banco:
        valor = float(input("Digite o valor a ser depositado: "))
        banco[numero_conta]['saldo'] += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")


def verificar_saldo():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in banco:
        saldo = banco[numero_conta]['saldo']
        print(f"O saldo da conta {numero_conta} é R$ {saldo:.2f}.")
    else:
        print("Conta não encontrada.")


def menu():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Verificar Saldo")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            verificar_saldo()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
