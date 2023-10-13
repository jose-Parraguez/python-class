from pathlib import Path

archivo = Path("08-archivos/prueba-archivo.txt")

texto = archivo.read_text().split("\n")

print(texto)

#para instertar texto en la linea 0 
texto.insert(0, "hola mundo")
archivo.write_text("\n".join(texto))