
#quebra de linha
#formatando decimais
#alterando virgulas e pontos 
#if else 
#operadores ternario


'''
#FIXME - concatenação com +
nome = "Pires"
idade = 17
altura = 1.80
#saida de dados
print("Olá,meu nome é " + str(nome) + ", e tenho" + str(idade))

#FIXME - concatenação com ,
print ("Olá meu nome é", nome, ", tenho", idade,"anos")

#FIXME - concatenação com f-string
print(f"Meu nome é {nome} e tenho {idade} anos de idade")

#eliminando quebra de linha
print("o sabio sabia ", end="")
print("que sabiá sabia assobiar")

valor = 1.7281871
#exibindo o valor com duas casas depois da virgula
print(f"{valor:,.3f}")

print(30*"_")
peso =input('Digite seu peso:').replace(',',".")
peso = float(peso)
print (f"Esse é seu peso {peso:.2f}")
'''
#Idade
'''
#if else
nome = str(input("Digite seu nome:"))
idade = int(input("Digite sua idade:"))
if idade >= 18:
    print(f"{nome} é maior de idade")
else:
    print(f"{nome} é menor de idade")  

''' 
#Média
'''
print(30*"_","Boletim ", 30*"_")
nome_aluno = str(input('Digite o nome do aluno:'))
nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))
nota4 = float(input('Digite a quarta nota'))

media = (nota1 + nota2 + nota3 + nota4)/4

# >=7 :aprovado
# <=5 : recuperação 
# reprovado 

if media >=7:
    print(f'{nome_aluno}!Aluno Aprovado')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f"Nota 3: {nota3} | NOta 4: {nota4}")
    print(20*'=')
    print(f"Média{media}")

elif media <=5:
    print(f'{nome_aluno}!Aluno de Recuperação')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f"Nota 3: {nota3} | NOta 4: {nota4}")
    print(20*'=')
    print(f"Média{media}")

else:
    print(f'{nome_aluno}!Aluno Reprovado')
'''

#EXERCICIO
'''
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
altura = float(input ('DIgite sua altura:'))

if idade >=12 and altura >= 1.3:
    print(f"A entrada de{nome} é permitida")
    
else:
    print(f'A entrada de{nome} não é permitida')
'''    
#Operadores ternarios
nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
#Verdadeiro ou Falso  
print(nome, "é maior de idade" if idade >=18 else 'é menor de idade')