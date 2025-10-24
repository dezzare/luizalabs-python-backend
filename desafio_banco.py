# DESAFIO
# 1   - O desafio consiste em deixar o código mais modularizado. 
# 2   - Criar as seguintes funções, como requisito mínimo: sacar, depositar, visualizar historico (extrato), criar usuário, criar conta corrente.
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


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    if numero_saques >= limite_saques:
        print("\n*** ERRO: Limite de saques excedido ***")

    elif valor > limite:
        print(f"\n*** ERRO: Valor a ser sacado excede o limite: {limite} ***")

    elif valor > saldo:
        print(f"\n*** ERRO: Saldo insuficiente: {saldo} ***")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"SAQUE: R${valor:.2f}\n"
        numero_saques += 1
        print("\n*** Saque realizado com sucesso *** ")
        print(f"*** Seu saldo atual é de: {saldo} ***")
    
    else:
        print("\nERRO: Valor informado é inválido")
    
    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n*** Depósito realizado com sucesso ***")
    else:
        print("\n*** ERRO: valor informado é inválido ***")

    return saldo, extrato

def imprime_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")




menu = """

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
                        saldo=saldo,
                        valor=valor,
                        extrato=extrato,
                        limite=limite,
                        numero_saques=numero_saques,
                        limite_saques=LIMITE_SAQUES,
                    )

    elif opcao == "2":
        valor = float(input("Informe o valor à ser depositado: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "3":
        imprime_extrato(saldo, extrato=extrato)

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")