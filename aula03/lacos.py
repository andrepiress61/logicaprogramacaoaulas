
#STUB - Problema:crie um sistema que calcule o indice de massa corporal(IMC) do usuario, mostre o valor do IMC na tela
#STUB - , e retorne esta no peso ideal, ou se precisa emagrecer ou engordar mais. Utilize a tabela do IMC
'''
nome = str(input("Digite seu nome:").upper())
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:").replace(",","."))

imc = (peso / (altura*altura))

print (f"Esse é seu IMC: {imc:.2f}")

if imc <=18.5:
    print(f"{nome} está abaixo do peso")
elif imc <=24.9:
    print(f"{nome} seu peso está ideal.")
elif imc <=29.9:
    print (f"{nome} está sobrepeso")
elif imc <=34.9:
    print(f"{nome} está com obesidade grau I")
elif imc <=39.9:
    print(f"{nome} está com obesidade grau II")
else:
    print(f"{nome} está com obesidade thais carla")
 
#REVIEW - Problema 2 : Elevador de carga possui capacidade para 200kg. 
Crie um programa que receba do usuario seu peso e o peso da carga e verifica se a carga 
está autorizada a usar o elevador ou não

limite = 200
peso_cli = float(input("Digite seu peso:"))
peso_car = float(input("Digite o peso da carga:"))

soma = peso_cli + peso_car

if soma >= limite:
    print ("Você não pode entrar no elavador")
else :
    print ("Você pode entrar no elevador")
'''

#NOTE - Lacos de repetição :
# loop
'''
while True:
    nome = str(input("Digite seu nome:").upper())
    peso = float(input("Digite seu peso:"))
    altura = float(input("Digite sua altura:").replace(",","."))

    imc = (peso / (altura*altura))

    print (f"Esse é seu IMC: {imc:.2f}")

    if imc <=18.5:
        print(f"{nome} está abaixo do peso")
    elif imc <=24.9:
        print(f"{nome} seu peso está ideal.")
    elif imc <=29.9:
        print (f"{nome} está sobrepeso")
    elif imc <=34.9:
        print(f"{nome} está com obesidade grau I")
    elif imc <=39.9:
        print(f"{nome} está com obesidade grau II")
    else:
        print(f"{nome} está com obesidade thais carla")
    opcao =input("Deseja calcular novamente? S - sim | N - não:").lower()
    if opcao == "s":
        continue
    elif opcao == "n":
        print('Saindo do sistema!')
        break 
    else:
        print("Opção invalida")
        break
'''
'''
nome = input("Digite seu nome:")
cpf = input("Digite seu cpf:")
telefone =input("Digite seu telefone:")
dt_nascimento = int(input(" Digite seu ano de nascimento:"))
print(40*"-")
while True:


    print(40*'-',"Programa do André",40*'-')
    print ()
    print('1 - Calculadora de IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz natal')
    print('6 - Sair')
    
    opcao = (input("Digite uma opcao: "))
    
    if opcao == "1":
        peso = float(input("Digite seu peso:"))
        altura = float(input("Digite sua altura:").replace(",","."))

        imc = (peso / (altura*altura))

        print (f"Esse é seu IMC: {imc:.2f}")

        if imc <=18.5:
            print(f"{nome} está abaixo do peso")
        elif imc <=24.9:
            print(f"{nome} seu peso está ideal.")
        elif imc <=29.9:
            print (f"{nome} está sobrepeso")
        elif imc <=34.9:
            print(f"{nome} está com obesidade grau I")
        elif imc <=39.9:
            print(f"{nome} está com obesidade grau II")
        else:
            print(f"{nome} está com obesidade thais carla")
    elif opcao == "2":
            ano_atual = 2025
            idade = ano_atual - dt_nascimento
            if idade >=18:
                print(f"{nome}é maior de idade," )
            else :
                print(f'{nome} é menor de idade')
            continue
    elif opcao == "3":
            while True:
                 print("CALCULADORA")
                 print("1 - SOMA")
                 print("2 - DIVISÃO")
                 print("3 - SUBTRAÇÃO")
                 print("4 - MULTIPLICAÇÃO")
                 print("5 - SAIR")

                 num1 = float(input("Digite o primeiro numero: ")) 
                 num2 = float(input("Digite o segundo numero: "))

                 opcao_calculo = int(input('Escolha uma operação: '))


                 if  opcao_calculo == 1:
                    print(f"{num1} + {num2} = {num1 + num2}")

                 elif opcao_calculo == 2:
                    print(f"{num1} - {num2} = {num1 - num2}")

                 elif opcao_calculo == 3:
                    print(f"{num1} X {num2} = {num2 * num1}")
                 elif opcao_calculo == 4:
                    print(f"{num1} / {num2} = {num1 / num2}")
                 elif opcao_calculo == 5:
                    print("Fechando sistema")
                    break
                 else :
                    print("Opção invalida")  
                    continue
    elif opcao == "4":
            print(f"Nome:{nome} | Telefone: {telefone}")
            print(f"CPF: {cpf}  | Data de NAscimento: {dt_nascimento}")
            continue
    elif opcao == "5":
            linha = 15
            j = 1
            while j<= linha:
                espacos = linha - j 
                estrelas = 2 * j - 1 
                print (" "* espacos + "*" * estrelas)
                j +=1
                continue
    elif opcao == "6":
            ("Saindo Sistema")
            break
    else:
            ("OPção invalida")
'''

nome = 'Andre'
for i in nome:
    print(i.replace(i,"*"))