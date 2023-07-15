frase = "hola mundo que pasa"

def quitar(texto):
    return [char for char in texto if char != " "]

def cuenta_caracteres(lista):
    char_dict = {}
    for char in lista:
        if char in char_dict:
            char_dict[char] += 1
        
        else:
            char_dict[char] = 1
    return char_dict 


def ordenados(dicts):
    return sorted(
        dicts.items(),
        key = lambda key: key[1],
        reverse = True,   
          )


pelo = quitar(frase)
contador = cuenta_caracteres(pelo)
orden = ordenados(contador)
print(orden)


