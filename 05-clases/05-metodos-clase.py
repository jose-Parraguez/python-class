class Perro:

    #propiedades de la clase
    patas = 4
    orejas = 2

    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")


    @classmethod
    def factory(cls):
        return cls("Chanchito feliz",4)
        
    

Perro.habla()

perro1 = Perro.factory()
print(perro1.edad,perro1.nombre)