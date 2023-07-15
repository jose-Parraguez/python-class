# se debe ocupar uppercase para no confundir al momento de llamarlas con una def
class Perro:

    #ya no se llaman funciones, al estar dentro de una clase ahora se llaman metodos 
    def habla(self):
        print("Guau")

mi_perro = Perro()

print(type(mi_perro))
mi_perro.habla()


print(isinstance(mi_perro,Perro))