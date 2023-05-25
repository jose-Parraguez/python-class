numeros = [1,2,3,4,5]

# esto esta mal o feo
    # hola = numeros [0]
    # print(hola)


primero,segundo, *otros = numeros
primero, *otros, ultimo = numeros

print(primero,ultimo,otros)