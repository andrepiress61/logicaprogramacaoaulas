import json
import os

class Livro:
    def __init__(self, id_livro: int, titulo: str, autor: str, ano: int):
        self.__id_livro = id_livro
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    # Encapsulamento com getters e setters
    @property
    def id_livro(self):
        return self.__id_livro

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    def to_dict(self):
        """Converte o objeto Livro em dicionário (para JSON)."""
        return {
            "id": self.__id_livro,
            "titulo": self.__titulo,
            "autor": self.__autor,
            "ano": self.__ano
        }
    
class Biblioteca:
    def __init__(self, arquivo_json="biblioteca.json"):
        self.__arquivo = arquivo_json
        self.__livros = []
        self.carregar_dados()

    def carregar_dados(self):
        """Carrega os livros do arquivo JSON."""
        if os.path.exists(self.__arquivo):
            with open(self.__arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                for d in dados:
                    livro = Livro(d["id"], d["titulo"], d["autor"], d["ano"])
                    self.__livros.append(livro)

    def salvar_dados(self):
        """Salva os livros no arquivo JSON."""
        dados = []  # lista vazia que vai guardar os dicionários

        # percorre cada livro da lista
        for livro in self.__livros:
            # transforma o objeto em dicionário e adiciona na lista
            dados.append(livro.to_dict())

        # agora 'dados' é uma lista de dicionários, pronta para salvar
        with open(self.__arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def gerar_id(self):
        """Gera um novo ID único para os livros."""
        if not self.__livros:
            return 1
        return max(l.id_livro for l in self.__livros) + 1

    # ----------- Operações CRUD -----------
    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro = Livro(self.gerar_id(), titulo, autor, ano)
        self.__livros.append(novo_livro)
        self.salvar_dados()
        print(f" Livro '{titulo}' cadastrado com sucesso!")

    def listar_livros(self):
        if not self.__livros:
            print("⚠ Nenhum livro cadastrado.")
        else:
            print("\n Lista de Livros:")
            for livro in self.__livros:
                print(f"ID: {livro.id_livro} | Título: {livro.titulo} | Autor: {livro.autor} | Ano: {livro.ano}")

    def atualizar_livro(self, id_livro, novo_titulo=None, novo_autor=None, novo_ano=None):
        for livro in self.__livros:
            if livro.id_livro == id_livro:
                if novo_titulo:
                    livro.titulo = novo_titulo
                if novo_autor:
                    livro.autor = novo_autor
                if novo_ano:
                    livro.ano = novo_ano
                self.salvar_dados()
                print("Livro atualizado com sucesso!")
                return
        print("Livro não encontrado.")

    def excluir_livro(self, id_livro):
        for livro in self.__livros:
            if livro.id_livro == id_livro:
                self.__livros.remove(livro)
                self.salvar_dados()
                print("Livro removido com sucesso!")
                return
        print("Livro não encontrado.")