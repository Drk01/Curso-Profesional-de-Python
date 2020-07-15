def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de Python 3".format(nombre)


def suma(val1, val2, val3):
    return val1 + val2 + val3


def obtener_curso():
    return "Curso de Python", "Básico", 3.5


print(crear_mensaje("Omar"))

print(suma(10, 20, 30))

curso, nivel, version = obtener_curso()

print(curso, nivel, version)
