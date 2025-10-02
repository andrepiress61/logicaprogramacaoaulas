from classe import Biblioteca


def main():
    biblioteca = Biblioteca()

    while True:
        print("\n===== Sistema de Gerenciamento de Biblioteca =====")
        print("1 - Cadastrar Livro")
        print("2 - Listar Livros")
        print("3 - Atualizar Livro")
        print("4 - Excluir Livro")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            try:
                ano = int(input("Ano: "))
                biblioteca.cadastrar_livro(titulo, autor, ano)
            except ValueError:
                print("Ano inválido, digite um número.")

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            try:
                id_livro = int(input("ID do livro a atualizar: "))
                titulo = input("Novo título (ou Enter p/ manter): ")
                autor = input("Novo autor (ou Enter p/ manter): ")
                ano = input("Novo ano (ou Enter p/ manter): ")
                biblioteca.atualizar_livro(
                    id_livro,
                    titulo if titulo else None,
                    autor if autor else None,
                    int(ano) if ano else None
                )
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "4":
            try:
                id_livro = int(input("ID do livro a excluir: "))
                biblioteca.excluir_livro(id_livro)
            except ValueError:
                print("Entrada inválida.")

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()