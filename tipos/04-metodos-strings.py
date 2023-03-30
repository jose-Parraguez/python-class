animal = " chanchito feliz "

print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal.strip())  # remueve espacios
print(animal.strip().capitalize())  # se pueden juntar varios o encadenar

print(animal.find("a"))
print(animal.replace("a", "p"))

print("a" in animal)
print("a" not in animal)
