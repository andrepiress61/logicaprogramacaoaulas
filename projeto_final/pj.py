import json
import os
#sistema de biblioteca, CRUD
limpar = os.system("cls") 
livros = []
novo_arquivo = " "
while True:
    try:
        def menu():
            print(20*"-", "MENU BIBLIOTECA", 20*"-")
            print("1 - Adicionar livro ")
            print("2 - Salvar o arquivo")
            print("3 - Encontrar livro ")
            print("4 - Atualizar livro ")
            print('5 - Excluir LIvro')
            print('6 - Sair')
        limpar
        menu()
        escolha = input("Escolha sua opcão:")

        def cadastrar_livro(livros):
            livro = {}
            livro['nome'] = input('informe o nome do livro: ').strip().title()
            livros.append(livro)
            print('Livro cadastrado com sucesso')

        def salvar_arquivo():
            global novo_arquivo
            novo_arquivo = input('informe o novo arquivo: ').strip().lower()
            with open(f'{novo_arquivo}.json', 'w', encoding='utf-8') as f:
                json.dump(livros, f, ensure_ascii=False, indent=4)
            print('arquivo salvo com sucesso...')

        def encontrar():
            novo_arquivo = str(input("Digite o nome do arquivo : "))
            with open(fr'{novo_arquivo}.json', "r", encoding='utf-8') as f:
                dados = json.load(f)               
                print (f"{dados}")

        def atualizar():
            ...

        def excluir():
            global livros, novo_arquivo
            excluir=[] 
            limpar()
            njson = input('insira o nome da tabela que deseja limpar: ').strip().lower()
            with open(fr'C:\Users\ead\Documents\Andreprograma\logicaprogramacaoaulas\projeto_final\{njson}', 'w', encoding= 'utf-8') as f:
            #substitui o json com uma lista vazia
                json.dump(excluir,f,ensure_ascii=False, indent=4)

            def sair():
                ...
        
        match escolha:
                # posiveis escolhas
                case "1":
                    cadastrar_livro(livros)             
                case "2":
                    salvar_arquivo()
                case '3':
                   encontrar()
                case '4':
                    ...

                case '5':
                    excluir()

                case '6':
                    print('Saindo...')
                    exit()

                # se a escolha for invalida
                case _:
                    print('Opção invalida.')


    except Exception as e:
        print(f"Erro: {e}")
        input('Pressione ENTER para continuar')
        
    

