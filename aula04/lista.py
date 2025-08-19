#lista 
'''
nome_lista = ['andre', 'cliclano', 'fulano', 'beltano', 'isabela', 'yasmin','andre']
nome = input ('Informe o nome que deseja encontrar:')

quantidade = nome_lista.count(nome)

try:
    print(f"{nome} foi encontrado na lista {quantidade} vezes")
except:
    print(f"{nome} não foi encontrado")

#alteração de valor na lista 
nome_lista = ['andre', 'cliclano', 'fulano', 'beltano', 'isabela', 'yasmin',]
nome_lista[0] = 'Alex'

for nome in nome_lista:
    print(nome)

nome_lista = ['andre', 'cliclano', 'fulano', 'beltano', 'isabela', 'yasmin']
nome_a_alterar = input("Informe o nome que deseja alterar:")
nome_lista[nome_lista.index(nome_a_alterar)] = input('Informe o novo nome:')

for nome in nome_lista:
    print(nome)

#REVIEW - Tabuada
numero = int(input("digite o numero"))

for i in range (1, 11):
    resultado = numero * i 
    print(f"{i} X {numero} = {resultado}")
'''

#contagem regressiva | importando bibliotecas 
#importandi bibliotecas (lib)
import os
from time import sleep 

cont = input ('Digite um numero inteiro:')

try:
    cont_int = int(cont)
    while cont_int >=0:
        os.system('cls')
        print(f" Contagem regressiva: {cont_int}...")
        sleep(1)
        cont_int -= 1
        os.system('cls')
except:
    print(' Digite um numero valido')

print("fim da sequencia ") 
