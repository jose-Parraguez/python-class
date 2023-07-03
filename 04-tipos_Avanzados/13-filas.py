from collections import deque

fila = deque([1,3,2,5])
fila.append(7)

print(fila)
print(type(fila))

fila.popleft()

print(fila)

if not fila:
    print("fila vacia")