numero = [
        [1,"felipe"],
        [5,"chanchito"],
        [3,"vaca"]
]


#la funcion lambda solo se utiliza para hacer una funcion solamente una vez en el codigo 
#tener muchas veces la palabra lambda en 1 codigo esta mal visto

numero.sort(key=lambda el:el[0], reverse= False)
print(numero)