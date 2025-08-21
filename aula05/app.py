import os

while True :
    try:
        os.system("cls")
        #entrada de dados
        etanol = float(input("Digite o preço do etanol:").replace(",","."))
        gasolina = float(input("digite o preço da gasolina:").replace(",","."))
        calculo = (etanol/gasolina)*100
        resultado = "Gasolina" if calculo > 70 else "etanol"

        print(f"Resultado = {calculo: .2f}%. Compensa abastecer com {resultado}.")

        opcao = input("Deseja refazer o calculo? (S/N)").lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
            case _:
                print(f"Opção invalida")
                continue
    except Exception as e:
        print(f"Não foi possivel executar a operação. {e}")
