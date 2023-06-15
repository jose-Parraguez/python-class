listaa = [
        [1,"felipe"],
        [5,"chanchito"],
        [3,"vaca"]
]

# nombres = []

# for lista in listaa:
#     nombres.append(lista[1])

# print(nombres)

#nombres = [usuario[1] for usuario in listaa]

#filtrar 
#nombres = [usuario[1] for usuario in listaa if usuario [0]>2] 

#filtrar y tranformar
nombres = [usuario[1] for usuario in listaa if usuario [0]>2]
print(nombres)


#map
nombres = list(map(lambda usuario:usuario[1],listaa))
print(nombres)

#filter
menosnombres = list(filter(lambda usuarios:usuarios[0] > 2, listaa))
menosnombres = list(map(lambda usuario:usuario[1],menosnombres))
print(menosnombres)