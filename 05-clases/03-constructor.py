class Perro:
    #contructor debe tener __init__
    def __init__(self, nombre, edad) :
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} con edad {self.edad} dice: Guau")

mi_perro = Perro("Pulgoso",1)
mi_perro2 = Perro("Coraje",2)

print(mi_perro.nombre)
mi_perro.habla()
mi_perro2.habla()
#print(mi_perro2.nombre)
