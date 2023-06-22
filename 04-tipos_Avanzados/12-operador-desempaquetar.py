# Para desempaquetar listas * 
lista = [1,2,3,4,5]

print(*lista)

#para desempaquetar diccionarios

punto1 = {"x" : 19,"z" : 50}
punto2 = {"y" : 30}

nuevopunto = {**punto1, **punto2, "P" : "perro"}
print(nuevopunto)