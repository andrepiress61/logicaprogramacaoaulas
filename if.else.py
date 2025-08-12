'''
concatenação
quebra de linha
formatando decimais
alterando virgulas e pontos 
if else 
operadores ternario
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
 

