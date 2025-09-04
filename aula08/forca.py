# biblioteca
import os 
import random
import json

# loop principal
while True:
    # trata os erros
    try:                 
        # função de menu
        def menu():
            # variavel global
            global escolha

            # menu
            print(20*"-", "MENU FORCA", 20*"-")
            print("1 - Animais ")
            print("2 - Objetos da cozinha ")
            print("3 - Comida ")
            print('4 - Sair')

            # usuario escolhe qual tema de forca
            escolha = input('Escolha um dos temas: ')
            
            # a variavel palavra randomiza uma palavra na lista palavras
            palavra = escolher_palavras(escolha)

            # chama a função de jogar
            jogar_forca(palavra)

        # função para escolher a palavra baseada no tema
        def escolher_palavras(escolha):
            # encontra o arquivo json
            with open ('palavras.json', 'r', encoding='utf-8') as f:
                # salva o resultado em uma variavel
                palavras = json.load(f)
            
            match escolha:
                # posiveis escolhas
                case "1":
                    # escolhe uma palavra na categoria animais
                    return random.choice(palavras["animais"])

                case '2':
                    # escolhe uma palavra na categoria objetos
                    return random.choice(palavras["objetos"])

                case '3':
                    # escolhe uma palavra na categoria comidas
                    return random.choice(palavras["comidas"])

                case '4':
                    print('Saindo...')
                    exit()

                # se a escolha for invalida
                case _:
                    print('Opção invalida.')

        # função de jogar
        def jogar_forca(palavra):
            # limpa tela
            os.system('cls' if os.name == 'nt' else 'clear')

            # variavel global
            global escolha

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

                print('Palavra escondida',palavra_escondida)
                print("Letras erradas",letras_erradas)
                print("Tentativas",tentativas)

                # se o usuario acertar a palavra
                if palavra_escondida == palavra:
                    print("Voce ganhou ")
                    menu()
                    break

                # se o usuario acabar com todas as tentativas
                elif tentativas == 0:
                    print(f"Você perdeu,a palavra era {palavra}")
                    menu()
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

        if __name__ == "__main__":
            # limpa tela
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()

    except Exception as e:
        print(f"Erro: {e}")
        input('Pressione ENTER para continuar')