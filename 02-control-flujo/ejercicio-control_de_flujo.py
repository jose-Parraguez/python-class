print("Bienvenidos a la calculadora \nPara salir escriba 'salir' \nLas Operaciones son suma, multi,div y resta'")

numero = input("Escribe el primer numero: ")
operacion = ""

while numero != "salir":
    operacion = input("Ingrese la operacion: ")
    numero = int(numero)

    if operacion == "suma":
        numero2 = int(input("Ingrese el segundo numero: "))
        numero = str(numero + numero2)
        print(f"El resultado es: {numero}")

    elif operacion == "resta":
        numero2 = int(input("Ingrese el segundo numero: "))
        numero = str(numero - numero2)
        print(f"El resultado es: {numero}")

    elif operacion == "multi":
        numero2 = int(input("Ingrese el segundo numero: "))
        numero = str(numero * numero2)
        print(f"El resultado es: {numero}")

    elif operacion == "div":
        numero2 = int(input("Ingrese el segundo numero: "))
        numero = str(numero / numero2)
        print(f"El resultado es: {numero}")

    elif operacion.lower() == "salir":
        print("saliste")
        break
