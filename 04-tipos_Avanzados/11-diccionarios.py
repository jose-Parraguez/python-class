#son una coleccion de datos que tiene un id y una llave
#es parecida a las bases de datos como entrega la informacion 

punto = {"x": 3, "y" : 5} 

#para acceder a el valor que quiero se pone la id
print (punto["x"])

#se pueden agregar llaves
punto["A"] = 45

print(punto)

# para preguntar si existe algo en el diccionario:
if "hola" in punto:
    print("encontre lala",punto["lala"])

# 
print(punto.get("x"))

#eliminar alguna llave
del punto["x"]
print(punto)

# con items se imprime la variable con el valor
for valor in punto.items():
    print (valor)


usuarios = [
    {"id":1, "nombre":"chanchito"},
    {"id":2, "nombre":"Perro"},
    {"id":3, "nombre":"Capibara"},
    {"id":4, "nombre":"Felipe"},
]

for usuario in usuarios:
    print(usuario["nombre"])