class Perro:

    #propiedades para que sean privadas, esto significa que no se puede cambiar el nombre desde afuera de
    #la clase
    def __init__(self, nombre, edad) :
        self.__nombre = nombre
        self.edad = edad

    #para acceder al valor de nombre
    def traer__nombre(self):
        return self.__nombre
    
    def habla(self):
        print(f"{self.__nombre} Guau!")


    @classmethod
    def factory(cls):
        return cls("Chanchito feliz",4)
        

perro1 = Perro.factory()
perro1.habla()

print(perro1.traer__nombre())