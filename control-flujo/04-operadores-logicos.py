# and, or , not

edad = 15

if edad > 14 and edad < 30:
    print("hola mundo")

gas = True
encendido = True
edad = 18

if gas and encendido:  # los 2 deben ser verdaderos
    print("puedes avanzar")

if gas or encendido:  # si 1 es verdadero ya puede avanzar
    print("puedes avanzar")

if not gas or encendido:  # si 1 es verdadero ya puede avanzar
    print("puedes avanzar")

if gas and (encendido or edad > 17):  # si 1 es verdadero ya puede avanzar
    print("puedes avanzar")
