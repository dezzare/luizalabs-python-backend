# DESAFIO
# 1   - O desafio consiste em deixar o código mais modularizado. 
# 2   - Criar as seguintes funções, como requisito mínimo: sacar, depositar, visualizar historico, criar usuário, criar conta corrente.
# 3   - Cada função terá uma regra de passagem de argumento.
# 3.1 - SAQUE: recebe argumentos somente por nome (keyword only). 
# 3.2 - DEPOSITAR: recebe argumentos por posição (positional only)
# 3.3 - EXTRATO: recebe argumentos por posição (saldo) e por nome (extrato)
# 4   - A função CRIAR USUARIO deverá seguir as seguintes regras:
# 4.1 - Usuários devem ser armazenados em uma LISTA
# 4.2 - Cada usuário é composto por: nome, data de nascimento, cpf e endereço.
# 4.3 - O endereço do usuário deverá ser uma string no formato: logradouro, número - bairro cidade/sigla estado.
# 4.4 - O CPF deve ser armazenado somente números
# 4.5 - Somente UM usuário por CPF
# 5   - A função CRIAR CONTA deverá seguir as seguintes regras:
# 5.1 - Contas devem ser armazenadas como uma LISTA.
# 5.2 - Cada conta é composta por: agência, número da conta e usuário.
# 5.3 - O número da conta deverá ser sequencial, iniciando em 1.
# 5.4 - O número da agência é fixo: "0001"
# 5.5 - USUÁRIO pode ter mais de uma conta.
# 5.6 - CONTA pertence somente a UM usuário.
# 6   - O retorno e a forma como serão chamadas pode ser definida a critério do desafiado.


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")