def mostrar_mensaje(mensaje):
    mensaje = mensaje.title()  # local

    def mostrar():
        print(mensaje)

    return mostrar


nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()


# Los closures son funciones que generan dinámicamente otra función. Estas funciones pueden acceder a las variables locales aún cuando la función que las haya ejecutado haya terminado.
