from usuarios import hola

# Cualquiera de las 2 opciones de abajo sirve para importar paquetes
from paquetes.acciones import caminar
from paquetes import acciones

from paquetes.subpaquetes.acciones2 import trotar
from paquetes.subpaquetes import acciones2


hola()

caminar()
acciones.caminar()

trotar()
acciones2.trotar()
