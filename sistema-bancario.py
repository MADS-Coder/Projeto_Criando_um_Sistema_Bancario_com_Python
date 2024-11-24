# Opções do que podem ser selecionadas do sistema
menu = """\n=== Sistema Bancário === 
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> """

saldo = 0
limite = 500
extrato = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1": 
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor 
            extrato += saldo 
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido! O depósito deve ser maior que zero.")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: R$ "))

        if LIMITE_SAQUES == 0:
             print("Limite diário de saques atingido!")
        elif valor > saldo:
            print("Saldo insuficiente!")
        elif valor > limite:
            print(f"O valor máximo por saque é R$ {limite:.2f}.")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            saldo -= valor
            extrato -= valor
            LIMITE_SAQUES -= 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "3":
        print("\n=== Extrato ===")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor digite novamente a opção desejada!.\n")