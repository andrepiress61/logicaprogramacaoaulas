import random
import string
def gerar_senha (comprimento=12, incluir_maisculo=True, incluir_minusculo=True,
                 incluir_numero=True , incluir_caracter=True):
    caracteres = ""
    if incluir_maisculo:
        caracteres += string.ascii_uppercase
    
    if incluir_minusculo:
        caracteres += string.ascii_lowercase

    if incluir_numero:
        caracteres += string.digits

    if incluir_caracter:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")
    
    senha="".join(random.choice(caracteres) for _ in range(comprimento))
    print(f"Senha gerada: {senha}")
    return senha

def main():
    print("Gerador de Senhas")
    comprimento = int(input("Digite o comprimento da senha (padrão 12): ") or 12)
    incluir_maisculo = input("Incluir letras maiúsculas? (s/n, padrão s): ").lower() != 'n'
    incluir_minusculo = input("Incluir letras minúsJculas? (s/n, padrão s): ").lower() != 'n'
    incluir_numero = input("Incluir números? (s/n, padrão s): ").lower() != 'n'
    incluir_caracter = input("Incluir caracteres especiais? (s/n, padrão s): ").lower() != 'n'

    senha = gerar_senha(comprimento, incluir_maisculo, incluir_minusculo,
                         incluir_numero, incluir_caracter)
    print(f"Sua nova senha é: {senha}")
    with open("senha.txt", "a") as s:
        s.write(f"{senha}\n")
    

if __name__ == "__main__":
    main() 
