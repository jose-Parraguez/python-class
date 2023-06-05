def hola(nombre, Apellido):
    print(f"hola {nombre} {Apellido}")


hola("Nicolas", "Parraguez")


def hola2(nombre, apellido="feliz"):
    print(f"hola {nombre} {apellido}")


hola2("Nicolas", "Parraguez")
hola2("Chanchito")  # esta es para ver parametros opcionales


def hola3(nombre, apellido="feliz"):
    print(f"hola {nombre} {apellido}")


hola3(apellido="Parraguez", nombre="Nicolas")
hola3("Chanchito")  # se asigna a que parametro se tiene que asignar la palabra
