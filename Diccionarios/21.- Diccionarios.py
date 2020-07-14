diccionario = {}

diccionario = {
    'total': 20,
    'descuento': True,
    'subtotal': 15
}

diccionario = {
    'total': 55, 10: 'Curso de Python', (1, 2, 3): True
}

# Obtener todas las llaves de nuestro diccionario
print(diccionario.keys())

# Obtener todos los valores del diccionario
print(diccionario.values())

# Obtener el valor del diccionario en valor a una llave
print(diccionario.get('tl', 'No existe la llave'))
