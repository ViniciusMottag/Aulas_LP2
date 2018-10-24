from abc import ABCMeta,abstractmethod
'''
Classe abstrata é um "rascunho" do que as classes que a herdaram devem ter e implementar
-Métodos abstratos devem, obrigatoriamente, ser implementados na classe que herdar.
'''
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def barulho(self):
        pass

class Cachorro(Animal):
    def barulho(self):
        print("Au au!")

class Gato(Animal):
    def barulho(self):
        print("Miaau")


class Fabrica:
    def monta_barulho(self, tipo_animal):
        #return Cachorro().barulho
        #return Gato().barulho
        return eval(tipo_animal)().barulho()
f = Fabrica()
animal = input('Qual animal você quer escutar? ')
f.monta_barulho(animal)