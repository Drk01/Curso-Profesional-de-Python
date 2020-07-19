class Animal:
    def comer(self):
        print('Comiendo')

    def dormir(self):
        print('Durmiendo')


class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print('Ladrando')

class Gato(Animal):
    def ronroneo(self):
        print('Ronroneo')


firulais = Perro('Furilais')
firulais.ladrar()
firulais.comer()
firulais.dormir()


bola_de_nieve = Gato()
bola_de_nieve.comer()
bola_de_nieve.dormir()