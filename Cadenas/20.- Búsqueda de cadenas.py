mensaje = "Este es un texto nu poco grande en cuanto a longitud de caracteres se refiere"

# Buscando la cantidad de veces que se repite una palabra

resultado = mensaje.count('texto')

# Buscando por el método in
resultado = "texto" in mensaje

# Usando el método find
resultado = mensaje.find('texto')

# Buscando si el texto está al principio del mensaje
resultado = mensaje.startswith('Este')

# Buscando si el texto está al final del mensaje
resultado = mensaje.endswith('e')

print(resultado)
