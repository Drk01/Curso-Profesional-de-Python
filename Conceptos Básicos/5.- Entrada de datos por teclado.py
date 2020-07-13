print('¿Cuál es tu nombre?')
nombre = input()

print('¿Cuántos años tienes?')
edad = int(input())

print('¿Cuántos Kg pesas?')
peso = float(input())

autorizado = input('¿Estás autorizado? \n') == 'si'

print("Hola", nombre)
print('Tu edad es ', edad, ' años')
print('Tu peso es ', peso)
print('Autorización', autorizado)
