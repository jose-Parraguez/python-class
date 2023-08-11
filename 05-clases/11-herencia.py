class animal:
    def comer(self):
        print("comiendo")


#se le llama herencia porque estoy ocupando los metodos de animal
class Perro(animal):
    def ladrar(self):
        print("Ladrando")
    

#Herencia-Multinivel toma todas las caracterisiticas de las clases
#no se debe hacer mas de 2 veces 
class Chanchito(Perro):
    def programar(self):
        print("programando")

chanchitos = Chanchito()
chanchitos.ladrar()