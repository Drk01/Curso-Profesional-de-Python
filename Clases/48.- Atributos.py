class Usuario:

    def __init__(self):
        self.username = ''
        self.correo = ''
        self.nombre = ''

    def saluda(self, nombre):
        return "Hola, soy un usuario " + self.nombre

    def mostrar_username(self):
        print(self.username)

    def crear_nombre(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(self.nombre)


cody = Usuario()
cody.username = 'cody'
cody.correo = 'codi@gmail.com'

cody.crear_nombre('Cody')
cody.mostrar_nombre()
