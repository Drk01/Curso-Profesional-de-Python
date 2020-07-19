def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1, maximo + 1):
        yield numero * posicion, numero, posicion


for resultado, numero, posicion in tabla_multiplicar(9):
    print(numero, "*", posicion, '=', resultado)

''' La palabra reservada a yield sirve para retornar valores sin detener la función '''
