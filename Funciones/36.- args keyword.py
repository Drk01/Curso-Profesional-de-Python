def suma(*args):
    total = 0
    for valor in args:
        total += valor

    return total

print(suma(10,10,10,10,10))