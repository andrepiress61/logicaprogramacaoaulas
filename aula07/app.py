#FUNÇÕES E MODULOS 
'''

def exibir_mensagem(nome):
    print(f"Olá {nome}, bem-vindo ao programa!")

nome = input("Digite seu nome: ")
decisao = input("Deseja ver a mensagem? (s/n): ")

match decisao:
    case 's' | 'S':
        exibir_mensagem(nome)
    case 'n' | 'N':
        print("Ok, até a próxima!")
        pass
    case _:
        print("Opção inválida. Por favor, responda com 's' ou 'n'.") 


def calcular_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

decisao = input("Deseja calcular o delta? (s/n): ").lower()
match decisao:
    case 's' | 'S':
        delta = calcular_delta(a, b, c)
        print(f"O valor do delta é: {delta}")
    case 'n' | 'N':
        print("Ok, até a próxima!")
        pass
    case _:
        print("Opção inválida. Por favor, responda com 's' ou 'n'.")
'''

#Crie uma aplicação de banco, onde o usuario se cadastra e cria uma conta corrente que começa com saldo de R$0,00. O usuario terá as opções: Criar conta, Exibir dados da conta, Depositar valor, Sacar valor, Encerrar valor, sair do programa.
import os 
import json 
limpar = os.system("cls")   
saldo = 0
nome = ""
conta_ativa = False

usuario = {}
def criar_conta():
    global nome, conta_ativa, cpf, telefone 
    nome = input('Digite o nome do usuário: ').strip()
    cpf = input('Digite o cpf do usuário: ').strip()
    telefone = input('Digite o telefone do usuário: ').strip()
    conta_ativa = True
    with open(fr"conta.json", "w", encoding='utf-8') as f:
        json.dump(nome, f,ensure_ascii=False, indent=4)

def exibir_dados():
    if conta_ativa:
        with open(fr"conta.json", "r", encoding='utf-8') as f:
            dados = json.load(f)
            print(f"Nome do usuário: {nome}")
            print(f"CPF do usuário: {cpf}")
            print(f"Telefone do usuário: {telefone}")
            print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Nenhuma conta ativa. Por favor, crie uma conta primeiro.")

def depositar_valor():
    global saldo
    if conta_ativa:
        valor = float(input("Digite o valor a ser depositado: R$ ").replace(',', '.'))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
        else:
            print("Valor inválido. O depósito deve ser maior que R$ 0,00.")
    else:
        print("Nenhuma conta ativa. Por favor, crie uma conta primeiro.")

def sacar_valor():
    global saldo
    if conta_ativa:
        valor = float(input("Digite o valor a ser sacado: R$ ").replace(',', '.'))
        if 0 < valor <= saldo:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Novo saldo: R$ {saldo:.2f}")
        elif valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor inválido. O saque deve ser maior que R$ 0,00.")
    else:
        print("Nenhuma conta ativa. Por favor, crie uma conta primeiro.")

def encerrar_conta():
    global nome, saldo, conta_ativa, cpf, telefone 
    if conta_ativa:
        if saldo == 0:
            with open(fr"conta.json", "w", encoding='utf-8') as f:
                f.write("")
            print(f"Conta de {nome} encerrada com sucesso.")
            conta_ativa = False
        else:
            print("Para encerrar a conta, o saldo deve ser R$ 0,00. Por favor, saque ou deposite o valor necessário.")
    else:
        print("Nenhuma conta ativa para encerrar.") 

limpar 

def menu():
    print("\n=== Menu do Banco ===")
    print("1. Criar conta")
    print("2. Exibir dados da conta")
    print("3. Depositar valor")
    print("4. Sacar valor")
    print("5. Encerrar conta")
    print("6. Sair do programa")
    escolha = input("Escolha uma opção (1-6): ")
    return escolha

while True:
    escolha = menu()
    match escolha:
        case '1':
            criar_conta()
        case '2':
            exibir_dados()
        case '3':
            depositar_valor()
        case '4':
            sacar_valor()
        case '5':
            encerrar_conta()
        case '6':
            print("Saindo do programa. Até a próxima!")
            break
        case _:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")

           