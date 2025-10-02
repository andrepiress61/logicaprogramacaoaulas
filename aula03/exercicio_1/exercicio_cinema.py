#pedi nome e idade
nome = str(input(f"DIgite seu nome: "))
idade = int(input(f"Digite sua idade: "))
#mostrar os filmes
while True:
    print(f"1 - | Invocação do mal          | classificação: 18 | sala: 6 |")
    print(f"2 - | Homem aranha              | classificação: L  | sala: 3 |")
    print(f"3 - | Coringa                   | classificação: 16 | sala: 1 |")
    print(f"4 - | Deadpool                  | classificação: 16 | sala: 4 |")
    print(f"5 - | Barraca do beijo          | classificação: 16 | sala: 2 |")

    print()
    #escolher o filme
    filme = int(input(f"Escolha o filme: "))
    #verificar a idade
    if filme == 1:
        if idade>=18:
            print("| ticket                          |")
            print("| Filme: premonição 6             |")
            print("| sala 6                          |")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            continue
    if filme == 2:
        print("| ticket                          |")
        print("| Filme: Quarteto fantastico      |")
        print("| sala 3                          |")
        break
    if filme == 3:
        if idade>=16:
            print("| ticket                          |")
            print("| Filme: Coringa                  |")
            print("| sala 1                          |")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            continue
    if filme == 4:
        if idade>=16:
            print("| ticket                          |")
            print("| Filme: Deadpool                 |")
            print("| sala 4                          |")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            continue
    if filme == 5:
        if idade>=16:
            print("| ticket                          |")
            print("| Filme: Creed                    |")
            print("| sala 2                          |")
            break
        else:
            print("Você não tem idade para assistir esse filme.")
            continue