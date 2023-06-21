#significa grupo o conjunto 
#coleccion de datos que no se puede repetir y no esta ordenado 
primer = {1,1,2,2,3,4}
print(type(primer))

print(primer)


#transformar a set una lista
segundo = [3,4,5]

segundo = set(segundo)
print(primer | segundo)

#solo devuelve los que se encuentran en los 2 set
print(primer & segundo)

#muestra solamente  los del primer grupo y se le quitan los del segundo
print(primer - segundo)


#diferencia simetrica 
print(primer ^ segundo)


#con los set no se puede ingresar a los datos
#segundo[0]
#pero se puede crear un if

if 5 in segundo:
    print("se encuentra")
else:
    print("no se encuentra")
