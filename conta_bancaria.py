menu = """
||===================||
||      Menu         ||
||  [d] - depóstio   ||
||  [s] - saque      ||
||  [e] - extrato    ||
||  [q] - sair       ||
||===================||
=>  """
extrato = ""
limite_saque = 500
LIMITE_SAQUES = 3
numero_saques = 0
saldo = 0

while True:


    opcao = input(menu)

    if opcao == 'd':

        valor = float(input("Informe o valor do depósito: "))


        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            f"Operação falhou! O valor informado é inválido."
    
    elif opcao == 's':
        
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            f"Operação negada, você não tem saldo suficiente!"

        elif excedeu_limite:
            f"Operação negada, o valor do saque é maior que o limite permitido!"

        elif excedeu_saque:
            f"Operação negada, número máximo de saque atingido!"

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1

        else:
            f"Operação inválida! O valor informado não é válido."
    
    elif opcao == 'e':
        f"\n================ EXTRATO ================"
        f"Não foram realizadas movimentações." if not extrato else extrato
        f"\nSaldo: R$ {saldo:.2f}"
        f"==========================================="


    elif opcao == 'q':
        break

    else:
        f"Operação inválida, selecione novamente a operação desejada!"
