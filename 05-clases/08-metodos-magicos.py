class Perro:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def __del__(self):
        print("Chao perro")


    def __str__(self) -> str:
        return f"hola soy Clase Perro: {self.nombre}" 

    def habla(self):
        print(f"{self.nombre}dice: Guau!")

perro = Perro("Chanchito",7)
print(perro)

del perro