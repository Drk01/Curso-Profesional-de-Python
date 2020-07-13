lista = [100, 200, 1, 2, 34, 5, 1.2, 1.3, 4.3]

# Ordenar la lista
lista.sort()
print(lista)

# Obteniendo el reverso de la lista
lista.sort(reverse=True)
print(lista)

# Obteniendo el número mayor
print(max(lista))

# Obteniendo el número menor
print(min(lista))

# Obteniendo el tamaño de la lista
print(len(lista))

# Buscando elemento en la lista
resultado = 1 in lista
print(resultado)

# Obteniendo el indice del numero buscado
print(lista.index(1))

# Obteniendo la cantidad de veces que se repite un número
print(lista.count(1))
