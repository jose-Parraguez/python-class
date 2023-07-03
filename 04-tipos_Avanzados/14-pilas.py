# una pila funciona parecido a una fila, pero la logica es diferente  
# solo funciona con append y con pop 

pila = [1,2]

pila.append(3)
pila.append(4)

#saco el elemento y lo pongo en la variable 
ultimo_elemeto = pila.pop()
ultimo_elemeto2 = pila.pop()
ultimo_elemeto3 = pila.pop()
ultimo_elemeto4 = pila.pop()


# imprimo las 2 para ver funcionamiento
print(pila)
print(ultimo_elemeto)

if not pila:
    print("No es una pila")
