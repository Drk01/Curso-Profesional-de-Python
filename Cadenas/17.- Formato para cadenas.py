texto = "curso de Python 3"

# Generar nuevo string con la letra inicial en mayúscula
resultado = texto.capitalize()
print(resultado)

# Generando un nuevo string en dónde las letras mayúsculas sean minúsculas y viceversa
resultado = texto.swapcase()
print(resultado)

# Convertir todas las letras a mayúsculas
resultado = texto.upper()
print(resultado)

# Convertir todas las letras a minúsculas
resultado = texto.lower()
print(resultado)

# Comprobar si el texto está en mayúsculas
resultado = texto.isupper()
print(resultado)

# Comprobar si el texto está en minúscula
resultado = texto.islower()
print(resultado)

# Generando un nuevo string con un formato de título
resultado = texto.title()
print(resultado)

# Reemplazando un string por otro
resultado = texto.replace('Python', 'Java')
print(resultado)

# Retornando un nuevo string sin los espacios al inicio y al final
resultado = texto.strip()
print(resultado)
