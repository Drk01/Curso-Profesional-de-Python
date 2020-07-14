tupla = (1, 2, 3, 4, 5, 6)
uno, dos, tres, *cuatro = tupla

# print(uno)
# print(dos)
# print(tres)
# print(cuatro)

lista = [10, 20, 30, 40]

resultado = zip(tupla, lista)

# Convertir a tupla
#resultado = tuple(resultado)

# Convertir a lista
# resultado = list(resultado)

print(resultado)
