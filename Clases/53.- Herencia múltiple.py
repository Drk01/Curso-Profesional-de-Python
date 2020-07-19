class Animal:
    def comer(self):
        print('Comiendo')

    def dormir(self):
        print('Durmiendo')


class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha


class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print('Ladrando')


class Gato(Animal, Mascota):
    def ronroneo(self):
        print('Ronroneo')


firulais = Perro('Furilais')
firulais.ladrar()
firulais.comer()
firulais.dormir()
firulais.fecha_adopcion('Hoy')

print(firulais.fecha_de_adopcion)
