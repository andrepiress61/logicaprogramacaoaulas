import json
import os 

usuarios = []
novo_arquivo = ""

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
#lista de usuários
while True:
    usuario = {}
    print (' 1 - Cadastrar um usuário')
    print (' 2 - salvar um arquivo JSON')   
    print (" 3 - Fazer leitura do JSON ")
    print (' 4 - Sair')

    opcao = input('Escolha uma opção: ')    
    limpar()

    match opcao:
        #processo de cadastro
        case '1':
            usuario ["nome"] = input('Digite o nome do usuário: ').strip()
            usuario ["idade"] = input('Digite a idade do usuário: ')
            usuario ["email"] = input('Digite o email do usuário: ').strip().lower()

            usuarios.append(usuario)
            limpar()
            print('Usuário cadastrado com sucesso!')
            continue

#salvando um arquico JSON
        case '2':   
            novo_arquivo = input('Digite o nome do arquivo : ').strip().lower()

            if novo_arquivo:
                with open(fr"aula06/{novo_arquivo}.json", "r", encoding='utf-8') as f:
                    dados_existentes = json.load(f)

            dados_existentes.extend(usuarios)

            with open(fr"C:\Users\ead\Documents\Andreprograma\logicaprogramacaoaulas\aula06/{novo_arquivo}.json", "w", encoding='utf-8') as f:
                json.dump(usuarios, f,ensure_ascii=False, indent=4)
            limpar()
            print(f'Arquivo salvo com sucesso!')
            continue

#fazendo a leitura do JSON
        case '3':
            if not novo_arquivo:
                novo_arquivo = input('Digite o nome do arquivo para leitura: ').strip().lower()
            with open(fr"C:\Users\ead\Documents\Andreprograma\logicaprogramacaoaulas\aula06/{novo_arquivo}.json", "r", encoding='utf-8') as f:
                dados = json.load(f)
            print(f'{"-" * 20} USUARIOS {"-" * 20}\n')
            for usuario in dados:
                for chave in usuario:
                    print(f'{chave.capitalize()}: {usuario.get(chave)}')
                print('-' * 40)
            continue

        case '4':
            print('Saindo...')
            break

        case _:
            print('Opção inválida! Tente novamente.')