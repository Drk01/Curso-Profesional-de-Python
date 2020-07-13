lenguajes = "Python; Java; Ruby; PHP; Swift; Javascript; C#; C; C++"

# Generando lista a partir de un string
resultado = lenguajes.split('; ')

# Generando string a partir de una lista
resultado = "; ".join(resultado)

texto = """Este es un 
texto con 
muchos 
saltos 
de 
línea
"""

resultado = texto.splitlines()

print(resultado)
