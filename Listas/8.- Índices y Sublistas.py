cursos = ['Python', 'Django', 'Flask', 'C', 'C++', 'C#', 'Java', 'PHP']

# Valores positivos en las listas.
cursoPython = cursos[0]

# Valores negativos en el índice retornan la lista a la inversa
cursoPHP = cursos[-1]

# Seleccionando intervalos en las listas
sub = cursos[0:3]

# Seleccionando elementos con saltos.
jump = cursos[1:7:2]

# Obteniendo el inverso de la lista
inverso = cursos[::-1]

print(cursos)
print(cursoPython)
print(cursoPHP)
print(sub)
print(jump)
print(inverso)