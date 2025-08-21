#importação
import json

try :
    arquivo = input("Digite o nome do arquivo :").strip().lower()

    with open(f"{arquivo}.json", "r" , encoding = "utf-8") as f:
        dados = json.load(f)

    print (f"{"-"*20} DADOS {"-"*20}\n")

    for chave in dados:
        print(f"{chave.captalize()}: {dados.get(chave)}")
    print(f"\n{"-"*40} FIM {"-"*40}")

except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")