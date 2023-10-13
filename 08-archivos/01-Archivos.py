from pathlib import Path
from time import ctime

archivo = Path("08-archivos/prueba-archivo.txt")

# print(archivo.stat())

print("acceso", ctime(archivo.stat().st_atime))