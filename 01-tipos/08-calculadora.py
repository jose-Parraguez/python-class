import math

n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))


suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = round(n1 / n2)
raiz1 = math.sqrt(n1)
raiz2 = math.sqrt(n2)

mensaje = f"""
Para los números {n1} y {n2},
el resutado de la suma es {suma}.
el resutado de la resta es {resta}.
el resutado de la multiplicacion es {multi}.
el resutado de la division es {div}.
la  raiz de {n1} es {raiz1}.
la  raiz de {n2} es {raiz2}.
"""

print(mensaje)
