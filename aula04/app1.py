
#NOTE - Programa: Sorteio V.1.0
#ANCHOR - Importando : bibliotecas 

#FIXME - random: escolha aleatoria 
#NOTE - Descricção : sistema recebe o nome dos candidatos e realiza o sorteio 
'''

#importandpo bibiliotecas 
import random

nome1 = input('Digite o primeiro nome:')
nome2 = input('Digite o segundo nome:')
nome3= input('Digite o terceiro nome:')
nome4 = input('Digite o quarto nome:')
nome5 = input('Digite o quinto nome:')

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(escolhido)

import random 

lista = []

sair = False

while sair ==False:
    nome_candidato = input ('Digite os nomes para o sorteio ou enter para sair :')
    if nome_candidato != "":
        #append - adiciona o valor da variavel dentro da lista
        lista.append(nome_candidato)
    else :
        sair = True
escolhido = random.choice(lista)
print (' O escolhido foi', escolhido)
#ANCHOR - 
import random
import os
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input ('Digite o nome para sorteio: ')
    if nome :
        lista_nomes.append(nome)
    else:
        break

while True :
    if lista_nomes:
        os.system('cls')
        escolhido = random.choice(lista_nomes)
        lista_sorteados.append(escolhido)

        print(f"O sorteado foi : {escolhido}")
        lista_nomes.remove(escolhido)
        opcao = input("Deseja sortear outro nome? \n S - sim \n N- não\n: ").lower()
        os.system('cls')

        if opcao != "s":
            break
    else:
        print('não há nomes para serem sorteado!')
        break
print (" Programa finalizado") 
print(f"O sorteados foram {lista_sorteados}")  
'''

#LINK - Programação
#LINK - 
#LINK - 
'''

from random import randint

print(" Tente adivinha um numero !")
num1 = input('Digite um numero: ')

num_secret = randint(1,10)

if num1 == num_secret:
    print (' Parabens ,você ganhou')
else:
    print ('Perdeu oatario')
    print (f'O numero correto era {num_secret}')
'''

#ANCHOR - Numero secreto
'''
import random
import os 
import time 
numero_secret = random.randint(1,100)

tenativas = 0
max_tenta = 10
acertou = False

print (60*"-")
print(f"Você tem {max_tenta} tentativas para adivinhar o numero secreto")
print(" Vamos começar ?")

while tenativas < max_tenta:
    try:
        palpite = int(input("Digite seu palpite: "))

    except ValueError:
        print ("Por favor, digite um numero valido")
        continue
    tenativas += 1

    if palpite == numero_secret:
        acertou = True
        break
    elif palpite< numero_secret :
        print("tente um numero maior")
        os.system("cls")
    else:
        print(' tente um numero menor')
        os.system("cls")
if acertou:
    print(f"Parabens ganhou, acertou o numero {numero_secret} em {tenativas} tentativas")

else:
    print(f"Perdeu vai se fuder otario, era o {numero_secret}")
'''
  
