import random
dano = random.randint(20,30)
# classe - espaço onde vou descrever um objeto
#atributos - caracteristicas do objeto
#metodos - ações desse objeto

#nome e vida - atacar
#self - quando quero me referir a algum atributo da classe
#construtor - qunado quero criar um novo objeto, chamo o construtor para acessar pos atributos 

class Personagem:
    #construtor 
    def __init__(self, nome, vida):
        #encapsulamento
        self.__nome = nome
        self.__vida = vida
 

    #defininfo GET 
    @property
    def nome(self):
        return self.__nome

    #definindo SET 
    @nome.setter
    def nome (self,novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida

    #definindo SET 
    @vida.setter
    def vida (self,novo_vida):
        self.__vida = novo_vida 
    
    @property
    def ataque(self, ataque):
        return self.__ataque
    
    @ataque.setter
    def ataque(self, ataque):
        self.__ataque = ataque

    @property
    def notificar(self):
        return self.__notificar
        
    @notificar.setter
    def notificar(self, notificar):
        self.__notificar = notificar
    
    def atacar(self,personagem):
        personagem.vida -= 20
        print(f"{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida ")
        print(f'Agora esta com {personagem.vida}')
'''
class PersonagemFavorito:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    #defininfo GET 
    @property
    def nome(self):
        return self.__nome

    #definindo SET 
    @nome.setter
    def nome (self,novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida

    #definindo SET 
    @vida.setter
    def vida (self,novo_vida):
        self.__vida = novo_vida 
    
    def atacar(self,personagem):
        personagem.vida -= 20
        print(f"{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida ")
        print(f'Agora esta com {personagem.vida}')
'''
class Guerreiro(Personagem):
    def __init__(self, nome, vida,ataque, escudo=False):
        super().__init__(nome, vida)
        self.ataque = ataque
        self.__escudo = escudo
        

    @property
    def escudo( self):
        return self.__escudo
        
    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo 

    def atacar(self, personagem):
        personagem.vida -= personagem.ataque
        print(f"{self.nome} atacou {personagem.nome} e tirou 40 pontos de vida ")
        if personagem.vida <= 1:
            print("Personagem morto")
        else:
            print(f'Agora esta com {personagem.vida}')
    
    def protecao(self, personagem):
        self.__vida += 10 

class Mago(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida)
        self.ataque = ataque
    
    def curar(self, personagem):
        personagem.vida += 15
        print (f"{self.nome} usou poder de cura em {personagem.nome}")
        print(f"A vida de {personagem.nome} agora é de {personagem.vida}")

    def atacar(self, personagem):
        personagem.vida -= personagem.ataque
        if personagem.vida <= 1:
            print("Personagem morto")
        else:
            print(f'Agora esta com {personagem.vida}')

class Caio(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida)
        self.ataque = ataque

    def fogo(self,personagem):
        personagem.vida -= dano
        print(f"{self.nome} queimou {personagem.nome}")
        print(f'Agora esta com {personagem.vida}')
        if personagem.vida <= 1:
            print("Personagem morto")
        else:
            print(f'Agora esta com {personagem.vida}')

    def atacar(self, personagem):
        personagem.vida -= personagem.ataque 
    

class Karython(Personagem):
    def __init__(self, nome, vida,ataque):
        super().__init__(nome, vida)
    
    def programar(self,personagem):
        personagem.vida -= 100000000000000000
        print (f"{self.nome} mandou {personagem.nome} direto para o SOE")
        print(f"Agora {personagem.nome} morreu por ter ido para o SOE")
        if personagem.vida <= 1:
            print("Personagem morto")
        else:
            print(f'Agora esta com {personagem.vida}')
 

    def notificar(self, personagem):
        personagem.ataque -= 20
        personagem.vida -= 20
        print (f"`{self.nome}, nerfou {personagem.nome}")

   
gandof = Mago("Gandof", 200, 100)
aragorn = Guerreiro('Aragorn',150, 100)
batuta = Caio('Batuta', 100,100)
karython = Karython("Karython", 131313,100)

karython.notificar(batuta)
karython.notificar(aragorn)
karython.notificar(gandof)

aragorn.atacar(batuta)
batuta.fogo(gandof)
gandof.atacar(batuta)


if batuta.vida <= 1:
    print("Batuta morreu")
elif gandof.vida <= 1:
    print('gandof morreu')
elif aragorn.vida <= 1:
    print('aragorn morreu')
else:
    pass 