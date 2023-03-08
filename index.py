class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class AnimalFactory:
    def criar_animal(self, tipo, nome=None, idade=None): #A ideia é que podemos criar vários tipos de animais com um só método
        if tipo == 'C':
            return Cachorro(nome, idade)
        elif tipo == 'G':
            return Passaro(nome,idade)
        elif tipo == 'P':
            return Gato(nome,idade)
    

class Cachorro(Animal):     
    def __init__(self, nome, idade): #Nesse sentido, delegamos a responsabilidade as classes filhas, caso haja necessidade de adição de algum animal
        super().__init__(nome,idade) #o processo se torna muito menos trabalhoso de ser implementado.
        self.tipo = 'Cachorro'
    

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.tipo = 'Gato'
    

class Passaro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.tipo = 'Passaro'
    


animal_factory = AnimalFactory()
while True:
    tipo = input("Digite o tipo de animal, C,G ou P: \n")
    if tipo == 'C' or tipo == 'G' or tipo == 'P':
        break
    else:  print ("Digite um tipo válido")

nome = input("Digite o nome do animal: \n")
idade = input("Digite a idade do animal: \n")

animal = animal_factory.criar_animal(tipo, nome, idade)
print (f"Nome: {animal.nome}\nIdade: {animal.idade}\nTipo {animal.tipo}")

