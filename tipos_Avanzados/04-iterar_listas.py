numeros = ["pelo","perro","raton"]


#imprimir la lista
for x in numeros:
    print(x)  

#ponerle un indice a la lista
for x in enumerate(numeros):
    print(x)  

#desempaquetar una lista
for indice, x in enumerate(numeros):
    print(indice,x)  