# Listas
# --------------------
"""
#        0  1  2  3
lista = [2, 5, 7, 5]

new_lista = [5, 10.5, "Hola", True]

valor = lista[0]
print(valor)
print(lista[2])

print(lista)
# lista[3] = 8
print(lista)

# Métodos de la lista

# append
lista.append(10)
print(lista)

# index
# print(lista.index(8))
# print(lista.index(100))

# count
print(lista.count(2))
print(lista.count(5))

# extend
lista.extend([7, 62, 20])
print(lista)

# insert
lista.insert(0, 14)
print(lista)

# remove
lista.remove(14)
print(lista)

lista.remove(5)
print(lista)

# lista.remove(100)

# pop
ultimo = lista.pop()
print(ultimo)
print(lista)

# sort
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)
"""

"""
# Tuplas
# ---------------------------

tupla = (5, 7, 8, 9)

# tupla[0] = 10

# index
print(tupla.index(8))

# count
print(tupla.count(9))
"""

"""
# Diccionarios
# ---------------------------

estudiante = {"nombre": "Pepe", "edad": 20, "carrera": "Ingeniería"}
print(estudiante["nombre"])
estudiante["nombre"] = "Pepe Trueno"
print(estudiante["nombre"])

print(estudiante)
estudiante["dni"] = 17854125
print(estudiante)

# get
print(estudiante.get("nombre"))
print(estudiante.get("fecha", "No hay valor"))
# print(estudiante["fecha"])

# keys
print(estudiante.keys())

# values
print(estudiante.values())

# items
print(estudiante.items())

# pop
print(estudiante.pop("dni"))
print(estudiante)

print(estudiante.pop("fecha", "No encontrado"))

# clear
estudiante.clear()
print(estudiante)
"""

# Conjuntos
# --------------------------

conjunto = {0, 2, 4, 4, 6}
print(conjunto)

pares = {0, 2, 4, 6, 8, 10}
impares = {0, 1, 3, 5, 7, 9}

# union
print(pares.union(impares))

# intersection
print(pares.intersection(impares))

# difference
print(pares.difference(impares))
