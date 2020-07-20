class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return 'Este objeto es un gato y su nombre es: '+self.nombre


class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return 'Este objeto es un pato y su nombre es: '+self.nombre


gato = Gato('Bigotes')
pato = Pato('Lucas')

print(gato.__dict__)
print(pato.__dict__)
