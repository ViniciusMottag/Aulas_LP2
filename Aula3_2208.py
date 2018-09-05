from random import randint
def lista():
    lista=[randint(0,100),randint(0,100)]
    return lista

print(lista())

class Animal():
    pass
meu_animal = Animal()
meu_animal.nome = "Rex"
meu_animal.tipo = "Urso"
meu_animal.cor = "Branco"

animal_da_fit = Animal()
animal_da_fit.nome = "Policia"
animal_da_fit.tipo = "Cachorro"
animal_da_fit.cor = "Preto"

#print(meu_animal)
#print(animal_da_fit)

print('Nome: ',meu_animal.nome) #Atributo
meu_animal.tipo="Dinossauro"
print('Tipo: ',meu_animal.tipo)

meu_animal.gosto_musical="Rock"
print('Do que ele gosta: ',meu_animal.gosto_musical)

novo_animal = meu_animal
novo_animal.nome = 'Josefa'
print('novo: ',novo_animal.nome)


class Pato:
    pass

pato=Pato()
patinho=Pato()

if pato == patinho:
    print("Estamos no mesmo endereço!")
else:
    print("Estamos em endereços diferentes")
print('Pato: ',pato)
print('Patinho: ',patinho)#RESP: C EXERCICIO
