from io import open


#escritura
# texto = "Hola mundo"

# archivo = open("08-archivos/hola_mundo.txt","w")
# archivo.write(texto)
# archivo.close()

#lectura

# archivo = open("08-archivos/hola_mundo.txt","r")
# texto = archivo.read()
# archivo.close()
# print(texto)


# archivo = open("08-archivos/hola_mundo.txt","r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)


#with
# with open("08-archivos/hola_mundo.txt","r") as archivo:
#     #print(archivo.readlines())
#     for linea in archivo:
#         print(linea)

#agregar
# archivo = open("08-archivos/hola_mundo.txt","a+")
# archivo.write("\n chao mundo ")
# archivo.close()

#lectura y escritura
# seek es para mover el puntero 
with open("08-archivos/hola_mundo.txt","r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto [0]