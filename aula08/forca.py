# biblioteca
import os 
import random
import json

# função para escolher a palavra baseada no tema
def escolher_palavras(escolha):
    # posiveis escolhas
    if escolha == "1":
        # encontra o arquivo json
        with open ('palavras.json', 'r', encoding='utf-8') as f:
            # salva o arquivo em uma variavel
            palavras = json.load(f)
            # escolhe uma palavra na categoria animais
            return random.choice(palavras["animais"])

    elif escolha == '2':
        # encontra o arquivo json
        with open ('palavras.json', 'r', encoding='utf-8') as f:
            # salva o arquivo em uma variavel
            palavras = json.load(f)
            # escolhe uma palavra na categoria objetos
            return random.choice(palavras["objetos"])

    elif escolha == '3':
        # encontra o arquivo json
        with open ('palavras.json', 'r', encoding='utf-8') as f:
            # salva o arquivo em uma variavel
            palavras = json.load(f)
            # escolhe uma palavra na categoria comidas
            return random.choice(palavras["comidas"])

    # se a escolha for invalida
    else:
        print('Opção invalida.')

# função de jogar
def jogar_forca():
    # limpa tela
    os.system('cls' if os.name == 'nt' else 'clear')

    # variavel global
    global escolha

    # a variavel palavra randomiza uma palavra na lista palavras
    palavra = escolher_palavras(escolha)
    letras_corretas =[]
    letras_erradas =[]
    tentativas = 6

    # loop
    while True:
        # limpa tela
        os.system('cls' if os.name == 'nt' else 'clear')

        # verifica se a letra escolhida foi a correta
        palavra_escondida = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra 

            else:
                palavra_escondida += "_"

        print('Palavra escondida', palavra_escondida)
        print("Letras erradas",letras_erradas)
        print("Tentativas", tentativas)

        # se o usuario acertar a palavra
        if palavra_escondida == palavra:
            print("Voce ganhou ")
            break

        # se o usuario acabar com todas as tentativas
        elif tentativas == 0:
            print(f"Você perdeu,a palavra era {palavra}")
            break

        # usuario escolhe uma letra
        letra_usuario = input("Digite uma letra ").lower()

        # verifica se a letra escolhida pelo usuario ta na palavra
        if letra_usuario in palavra:
            print("Letra correta ")
            letras_corretas.append(letra_usuario)

        # se a letra escolhida nao esta na palavra
        else:
            print("Letra errada")
            letras_erradas.append(letra_usuario)
            tentativas -= 1
            
# função de menu
def menu():
    # variavel global
    global escolha

    # menu
    (20*"-", "MENU FORCA", 20*"-")
    print("1 - Animais ")
    print("2 - Objetos da cozinha ")
    print("3 - Comida ")
    
    # usuario escolhe qual tema de forca
    escolha = input('Escolha um dos temas: ')
    
    # chama a função de jogar
    jogar_forca()

if __name__ == "__main__":
    # limpa tela
    os.system('cls' if os.name == 'nt' else 'clear')
    menu()